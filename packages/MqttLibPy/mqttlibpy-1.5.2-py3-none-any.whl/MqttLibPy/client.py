import json
import hashlib
import traceback

from psycopg2 import InterfaceError

from paho.mqtt.publish import single
from paho.mqtt.client import MQTTv5, Client, MQTTMessage
from cryptography.fernet import Fernet

from logging import getLogger
from typing import Union, List, Tuple

from .serializer import Serializer
from enum import Enum
from time import sleep

class MqttReturnCode(Enum):
    MQTT_ERR_AGAIN = -1
    MQTT_ERR_SUCCESS = 0
    MQTT_ERR_NOMEM = 1
    MQTT_ERR_PROTOCOL = 2
    MQTT_ERR_INVAL = 3
    MQTT_ERR_NO_CONN = 4
    MQTT_ERR_CONN_REFUSED = 5
    MQTT_ERR_NOT_FOUND = 6
    MQTT_ERR_CONN_LOST = 7
    MQTT_ERR_TLS = 8
    MQTT_ERR_PAYLOAD_SIZE = 9
    MQTT_ERR_NOT_SUPPORTED = 10
    MQTT_ERR_AUTH = 11
    MQTT_ERR_ACL_DENIED = 12
    MQTT_ERR_UNKNOWN = 13
    MQTT_ERR_ERRNO = 14
    MQTT_ERR_QUEUE_SIZE = 15
    MQTT_ERR_KEEPALIVE = 16


class MqttClient:

    def __init__(self, hostname: str, port: int, prefix: str = "", suffix: str = "", uuid="",
                 encryption_key: bytes = '',
                 encryption_callback=None, qos=2, client_id=""):
        self.prefix = prefix
        self.suffix = suffix
        self.uuid = uuid
        self.qos = qos
        self.client_id = client_id

        self.hostname = hostname
        self.port = port
        self.encryption_key = encryption_key
        if encryption_callback:
            self.encryption_callback = encryption_callback
        else:
            self.encryption_callback = None

        self.routes = []
        self.files = {}

        self.client = Client(client_id, userdata=None, protocol=MQTTv5)

        def _on_connect(client: Client, _, __, ___, ____):
            for route in self.routes:
                client.subscribe(route)

        self.client.on_connect = _on_connect

        self._connected_for_send = False

        self.logger = getLogger("Mqtt Client")

    def send_message(self, topic: str, payload: dict) -> Union[MqttReturnCode, int]:
        print(f'Sending message to {topic}')
        json_payload = json.dumps(payload)

        return self._send_string_rc(topic, json_payload)

    def send_message_serialized(self, message: Union[List[dict], str], route,
                                encodeb64: bool = False, valid_json=False, error=False, secure=False) -> List[MqttReturnCode]:
        """
        :param message: List of dicts or string to send.
        :param route: topic to send message to
        :param encodeb64: Not implemented
        :param valid_json: Indicates "message" is a valid parsable json (list[dict])
        :param error: Indicates this is an error message

        :return: List of return codes
        """
        json_messages = Serializer(self.uuid, self.encryption_key or self.encryption_callback and self.encryption_callback(route)).serialize(message, encodeb64, valid_json, is_error=error, encrypt=secure)

        rcs = []
        for serialized_message in json_messages:
            rc = self.send_message(route, serialized_message)
            rcs.append(rc)

        return rcs

    def _send_string(self, topic: str, payload: Union[str, bytes]):
        print(f"Sending string to {topic}")
        single(topic, payload, hostname=self.hostname, port=self.port, protocol=MQTTv5, qos=self.qos)

    def _connect_for_send(self):
        self.client.connect(self.hostname, self.port)
        self.client.loop_start()
        sleep(0.5)

        self._connected_for_send = True

    def _send_string_rc(self, topic: str, payload: Union[str, bytes]) -> Union[MqttReturnCode, int] :
        is_connected = self.client.is_connected()
        if not is_connected:
            self._connect_for_send()

        res = self.client.publish(topic, payload)

        if res.rc != MqttReturnCode.MQTT_ERR_SUCCESS.value:
            self.logger.error(f"Error sending message to {topic}, code: {res.rc}")

        err_code = res.rc
        try: 
            err_code = MqttReturnCode(res.rc)
        except ValueError:
            self.logger.warning(f"Unknown error code: {res.rc}")

        if self._connected_for_send:
            self.client.disconnect()

        return err_code

    def send_bytes(self, message: bytes, route: str, filename: str = '', metadata: dict = None, secure=False) -> Tuple[List[MqttReturnCode], List[MqttReturnCode]]:
        if metadata is None:
            metadata = {}

        rcs = []
        metadata_rcs = []
        # Mandar la metadata por route y el archivo por route/
        serialized_message = (Serializer(self.uuid, self.encryption_key or self.encryption_callback and self.encryption_callback(route))
                              .serialize(message, filename=filename, metadata=metadata, encrypt=secure))

        for msg in serialized_message:
            if secure and (self.encryption_key or self.encryption_callback):
                message = self._get_fernet(route).encrypt(message)
            elif secure:
                raise Exception("No encryption key was provided to the client in order to send an encrypted message")

            metadata_rcs.append(self.send_message(route, msg))
            rc = self._send_string_rc(f"{route}/file", message)
            rcs.append(rc)

        return rcs, metadata_rcs

    def send_file(self, route: str, filepath: str, metadata: dict = None, secure=False) -> List[MqttReturnCode]:
        if metadata is None:
            metadata = {}
        with open(filepath, "rb") as f:
            file_name = f.name.split("/")[-1]
            file_bytes = f.read()
        print(f"Sending {file_name} of length {len(file_bytes)}")
        return self.send_bytes(file_bytes, route, file_name, metadata, secure=secure)

    def register_route(self, route, callback, pure_route=False):
        if not pure_route:
            topic = f'{self.prefix}{route}{self.suffix}'
        else:
            topic = route

        self.routes.append(topic)
        print(f"Listening to topic: {topic}")
        self.client.message_callback_add(topic, callback)

    def listen(self):
        print(f"Connecting to {self.hostname}:{self.port} as {self.client_id}")
        self.client.connect(self.hostname, self.port)
        self.client.loop_forever()

    def endpoint(self, route: str, force_json=False, is_file=False, secure=False, endpoint_encryption_callback=None, pure_route=False):
        """
        :param route: part of the route to listen to, the final route will be of the form {prefix}{route}{suffix}
        :param force_json: The message payload is in json format, and will be passed to the callback as a dict
        :param is_file: Indicates if the type of payload is a bytes object
        :param secure: Whether to decrypt payloads with the provided key or not
        :param endpoint_encryption_callback: Custom encryption callback for this specific endpoint
        :return:
        """
        def decorator(func):
            def wrapper_json(client: Client, _, message: MQTTMessage):
                try:
                    parsed_message = json.loads(message.payload)
                    encryption_key = (self.encryption_key or self.encryption_callback
                                      and self.encryption_callback(message.topic))
                    if endpoint_encryption_callback:
                        encryption_key = endpoint_encryption_callback(message.topic)
                    if secure:
                        parsed_message['data'] = (Serializer(self.uuid, encryption_key)
                                                  .decrypt_str(parsed_message['data']))
                        parsed_message['data'] = json.loads(parsed_message['data'])
                    return func(client, _, parsed_message['data'])
                except InterfaceError as e:
                    self.logger.error(f"Error in json endpoint {route}")
                    self.logger.error(e)
                    tb = traceback.format_exc()
                    self.logger.error(tb)
                    raise InterfaceError("Database error, re initializing cursor")
                except Exception as e:
                    self.logger.error(f"Error in json endpoint {route}")
                    self.logger.error(e)
                    tb = traceback.format_exc()
                    self.logger.error(tb)

            def wrapper_files(client: Client, user_data, message):
                try:
                    if secure:
                        file_bytes = self._get_fernet(message.topic).decrypt(message.payload)
                    else:
                        file_bytes = message.payload
                    md5_hash = hashlib.md5(file_bytes).hexdigest()
                    if md5_hash in self.files:
                        self.files[md5_hash]['bytes'] = file_bytes
                    else:
                        # File arrived before the metadata, this shouldn't happen
                        self.logger.warning(f"File arrived before metadata. Hash: {md5_hash}")
                        self.files[md5_hash] = {}
                        self.files[md5_hash]['bytes'] = file_bytes
                        return

                    func(client, user_data, self.files[md5_hash])

                    # Cleanup
                    del self.files[md5_hash]
                except Exception as e:
                    self.logger.error(f"Error in file endpoint {route}")
                    self.logger.error(e)
                    tb = traceback.format_exc()
                    self.logger.error(tb)

            def wrapper_files_metadata(client: Client, user_data, message):
                try:
                    parsed_message = json.loads(message.payload)
                    if secure:
                        bytes_json = self._get_fernet(message.topic).decrypt(parsed_message['data'].encode('utf-8'))
                        string_json = bytes_json.decode('utf-8')
                        parsed_message['data'] = json.loads(string_json)

                    if not isinstance(parsed_message['data'], dict):
                        parsed_message['data'] = json.loads(parsed_message['data'])

                    if parsed_message['type'] != 'file':
                        self.logger.warning(
                            f"A message of type {parsed_message['type']} was received on a file endpoint")
                        return

                    if parsed_message['md5_hash'] in self.files:
                        # Metadata arrived late
                        self.files[parsed_message['md5_hash']]['md5_hash'] = parsed_message['md5_hash']
                        self.files[parsed_message['md5_hash']]['filename'] = parsed_message['data']['filename']
                        self.files[parsed_message['md5_hash']]['from'] = parsed_message['from']
                        self.files[parsed_message['md5_hash']]['data'] = parsed_message['data']
                        func(client, user_data, self.files[parsed_message['md5_hash']])
                        del self.files[parsed_message['md5_hash']]
                    else:
                        self.files[parsed_message['md5_hash']] = {
                            'md5_hash': parsed_message['md5_hash'],
                            'filename': parsed_message['data']['filename'],
                            'from': parsed_message['from'],
                            'bytes': b'',
                            'data': parsed_message['data']
                        }
                except Exception as e:
                    self.logger.error(f"Error in metadata endpoint {route} {e}")
                    tb = traceback.format_exc()
                    self.logger.error(tb)

            if force_json:
                self.register_route(route, wrapper_json, pure_route=pure_route)
            elif is_file:
                self.register_route(route, wrapper_files_metadata, pure_route=pure_route)
                self.register_route(f"{route}/file", wrapper_files, pure_route=pure_route)
            else:
                self.register_route(route, func, pure_route=pure_route)

            def inner(*args, **kwargs):
                pass

            return inner

        return decorator

    def _get_fernet(self, topic: str) -> Union[None, Fernet]:
        key = self.encryption_key or self.encryption_callback(topic)
        if key is None:
            self.logger.warning("No encryption KEY was provided")

        fernet = Fernet(key)

        if fernet is None:
            self.logger.warning("Fernet client couldnt be initialized, check if the KEY is valid")

        return fernet

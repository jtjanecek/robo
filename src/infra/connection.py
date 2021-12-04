import asyncio
from utils.rtbufferdeframer import RtBufferDeframer
from enums.enums import MediusPlayerStatus
from queue import Queue
from datetime import datetime
from infra.game import Game
import logging
logger = logging.getLogger("robo.connection")

class Connection:
    def __init__(self, server_name: str, writer: asyncio.StreamWriter):
        # Server info
        self.server_name = server_name
        self.writer = writer
        self.addr = self.writer.get_extra_info('peername')[0]
        self.port = self.writer.get_extra_info('peername')[1]
        # Encryption
        self._rsa = None
        self._rc4 = None
        self._server_rc4 = None

    def set_rsa(self, client_rsa):
        self._rsa = client_rsa

    def get_rsa(self):
        return self._rsa

    def set_rc4(self, client_rc4):
        self._rc4 = client_rc4

    def get_rc4(self):
        return self._rc4

    def set_server_rc4(self, server_rc4):
        self._server_rc4 = server_rc4

    def get_server_rc4(self):
        return self._server_rc4

    def __str__(self):
        return f'Connection({self.server_name} | {self.addr} | {self.port})'

    def close(self):
        pass

class UdpConnection(Connection):
    def __init__(self, server_name, transport, addr):
        self.server_name = server_name
        self.addr = addr[0]
        self.port = addr[1]
        self.transport = transport

    def __str__(self):
        return f'UdpConnection({self.server_name} | {self.addr} | {self.port})'

    def send(self, data):
        self.transport.sendto(data, (self.addr, self.port))

    def hash(self):
        return self.__str__()
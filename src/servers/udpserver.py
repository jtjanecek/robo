from time import sleep
import asyncio
import os
import threading
import asyncio
from infra.connection import UdpConnection
import traceback

import logging
from logging import handlers


class UDPServer:
    def __init__(self, monolith, name, port, log_maxb_mb, log_backup_count, log_location):

        self._logger = logging.getLogger(f"robo.{name}")
        formatter = logging.Formatter('%(asctime)s %(name)s | %(levelname)s | %(message)s')
        filehandler = handlers.RotatingFileHandler(os.path.join(log_location,f'{name}.log'), mode='w', maxBytes=log_maxb_mb*1000000, backupCount=log_backup_count)
        filehandler.setLevel(logging.DEBUG)
        filehandler.setFormatter(formatter)
        self._logger.addHandler(filehandler)

        self._monolith = monolith
        self._name = name
        self._ip = '0.0.0.0'
        self._port = port

    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        connection = UdpConnection(self._name, self.transport, addr)
        self._logger.debug(f"{self._name} | {connection} | I | {data.hex().upper()}")

        try:
            packets = self._monolith.process_udp(connection, data, self._logger)

            p = b''
            for packet in packets:
                self._logger.debug(f"{self._name} | {connection} | O | {packet.hex().upper()}")
                p += packet
            if p != b'':
                self.transport.sendto(p, addr)

        except Exception as e:
            self._logger.exception(f"Exception on connection: {connection}")

    async def start(self):
        self._logger.info(f'Serving on {(self._ip, self._port)} ...')
        await asyncio.get_event_loop().create_datagram_endpoint(lambda: self, local_addr=(self._ip, self._port))

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
	def __init__(self, monolith, name, ip, port, log_maxbytes, log_backup_count):

		self._logger = logging.getLogger(f"robo.{name}")
		formatter = logging.Formatter('%(asctime)s %(name)s | %(threadName)s | %(levelname)s | %(message)s')
		filehandler = handlers.RotatingFileHandler(os.path.join('logs',f'{name}.log'), mode='w', maxBytes=log_maxbytes, backupCount=log_backup_count)
		filehandler.setLevel(logging.DEBUG)
		filehandler.setFormatter(formatter)
		self._logger.addHandler(filehandler)

		self._monolith = monolith
		self._name = name
		self._ip = ip
		self._port = port
		self._thread = threading.Thread(target = self.start)
		self._thread.setDaemon(True)
		self._thread.start()

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

	def start(self):
		loop = asyncio.new_event_loop()
		asyncio.set_event_loop(loop)
		task = loop.create_datagram_endpoint(lambda: self, local_addr=(self._ip, self._port))
		self._logger.info(f'Serving on {(self._ip, self._port)} ...')
		loop.run_until_complete(task) # Server starts listening
		loop.run_forever()

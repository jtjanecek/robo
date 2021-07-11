from time import sleep
import asyncio
import os
import threading
import asyncio
from infra.connection import UdpConnection
import traceback

import logging
logger = logging.getLogger("robo.udp")
formatter = logging.Formatter('%(name)s | %(threadName)s | %(levelname)s | %(message)s')
filehandler = logging.FileHandler(os.path.join('logs','udp.log'), mode='w')
filehandler.setLevel(logging.DEBUG)
filehandler.setFormatter(formatter)
logger.addHandler(filehandler)

class UDPServer:
	def __init__(self, monolith, name, ip, port):
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
		logger.debug(f"{self._name} | {connection} | I | {data.hex().upper()}")

		try:
			packets = self._monolith.process_udp(connection, data)

			for packet in packets:
				logger.debug(f"{self._name} | {connection} | O | {data.hex().upper()}")
				self.transport.sendto(packet, addr)

		except Exception as e:
			logger.exception(f"Exception on connection: {connection}")

	def start(self):
		loop = asyncio.new_event_loop()
		asyncio.set_event_loop(loop)
		task = loop.create_datagram_endpoint(lambda: self, local_addr=(self._ip, self._port))
		logger.info(f'{self._name} | Serving on {(self._ip, self._port)} ...')
		loop.run_until_complete(task) # Server starts listening
		loop.run_forever()

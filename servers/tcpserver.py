import os
import threading
import time
import asyncio
from infra.connection import Connection
import traceback

import logging
logger = logging.getLogger("robo.tcp")
formatter = logging.Formatter('%(name)s | %(threadName)s | %(levelname)s | %(message)s')
filehandler = logging.FileHandler(os.path.join('logs','tcp.log'), mode='w')
filehandler.setLevel(logging.DEBUG)
filehandler.setFormatter(formatter)
logger.addHandler(filehandler)

class TCPServer:
	def __init__(self, monolith, name, ip, port):
		self._monolith = monolith
		self._name = name
		self._ip = ip
		self._port = port
		self._thread = threading.Thread(target = self.start)
		self._thread.setDaemon(True)
		self._thread.start()


	async def handle_incoming(self, reader, writer):
		connection = Connection(self._name, writer)

		logger.info(f"Client connected: {connection}")

		try:
			while True:
				data = await asyncio.wait_for(reader.read(1024), timeout=45)

				if data == b'':
					break;

				# Analyze incoming data
				message = data.hex().upper()
				logger.debug(f"{connection} | I | {message}")

				packets = self._monolith.process_tcp(connection, data)

				for packet in packets:
					logger.debug(f"{connection} | O | {packet.hex().upper()}")
					writer.write(packet)
					
				if len(packets) != 0:
					await writer.drain()

		except asyncio.TimeoutError as te:
			logger.info(f"Client timed out: {connection}")
		except Exception as e:
			logger.error(f"Exception on connection: {connection}")
			logger.error(e, exc_info=True)
		finally:
			self._monolith.client_disconnected(connection)
			logger.info(f"Client disconnected: {connection}")

			connection.close()
			writer.close()
			await writer.wait_closed()

	async def looper(self):
		server = await asyncio.start_server(
		self.handle_incoming, self._ip, self._port)
	
		addr = server.sockets[0].getsockname()
		logger.info(f'{self._name} | Serving on {addr} ...')

		async with server:	
			await server.serve_forever()

	def start(self):
		asyncio.run(self.looper())

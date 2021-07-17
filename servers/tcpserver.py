import os
import threading
import time
import asyncio
from infra.connection import Connection
import traceback
import logging
from logging import handlers



class TCPServer:
	def __init__(self, monolith, name, ip, port):

		self._logger = logging.getLogger(f"robo.{name}")
		formatter = logging.Formatter('%(asctime)s %(name)s | %(levelname)s | %(message)s')
		filehandler = handlers.RotatingFileHandler(os.path.join('logs',f'{name}.log'), mode='w', maxBytes=1000000, backupCount=5)

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


	async def handle_incoming(self, reader, writer):
		connection = Connection(self._name, writer)

		self._logger.info(f"Client connected: {connection}")

		try:
			while True:
				data = await asyncio.wait_for(reader.read(1024), timeout=45)

				if data == b'':
					break;

				# Analyze incoming data
				message = data.hex().upper()
				self._logger.debug(f"{connection} | I | {message}")

				packets = self._monolith.process_tcp(connection, data, self._logger)

				framed = b''
				for packet in packets:
					self._logger.debug(f"{connection} | O | {packet.hex().upper()}")
					framed += packet
				if framed != b'':
					writer.write(framed)
					await writer.drain()

		except asyncio.TimeoutError as te:
			self._logger.info(f"Client timed out: {connection}")
		except Exception as e:
			self._logger.exception(f"Exception on connection: {connection}")
		finally:
			try:
				self._monolith.client_disconnected(connection)
				self._logger.info(f"Client disconnected: {connection}")

				connection.close()
				writer.close()
				await writer.wait_closed()
			except Exception as e:
				self._logger.exception(f"Exception on connection: {connection}")
				
	async def looper(self):
		server = await asyncio.start_server(
		self.handle_incoming, self._ip, self._port)
	
		addr = server.sockets[0].getsockname()
		self._logger.info(f'Serving on {addr} ...')

		async with server:	
			await server.serve_forever()

	def start(self):
		asyncio.run(self.looper())

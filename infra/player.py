from utils.rtbufferdeframer import RtBufferDeframer
import asyncio
from queue import Queue
from enums.enums import MediusPlayerStatus

import logging
logger = logging.getLogger("robo.player")

class Player():
	def __init__(self, account_id, username, session_key, mls_world_id, mls_con):
		# Basic info
		self._account_id = account_id
		self._username = username
		self._session_key = session_key
		self._mls_world_id = mls_world_id
		self._status = MediusPlayerStatus.MEDIUS_PLAYER_IN_CHAT_WORLD

		# Connection info
		self._mls_connection = mls_con
		self._dmetcp_connection = None
		self._dmeudp_connection = None

		# Buffers for packet fragmentation
		self._mls_deframe_buffer = RtBufferDeframer()
		self._dmetcp_deframe_buffer = RtBufferDeframer()
		self._dmeudp_deframe_buffer = RtBufferDeframer()

		# Game info
		self._game = None
		self._dmeudp_queue = Queue()
		self._dmetcp_aggtime = 0.03
		self._dmeudp_aggtime = 0.03
		self._dmetcp_flush_task = None
		self._dmeudp_flush_task = None

	def send_mls(self, data: bytes):
		self._mls_connection.writer.write(data)
		asyncio.create_task(self.mlsflusher())

	async def mlsflusher(self):
		await self._dmetcp_connection.writer.drain()

	def start_tcpflusher(self):
		self._dmetcp_flush_task = asyncio.create_task(self.tcpflusher())

	def start_udpflusher(self):
		self._dmeudp_flush_task = asyncio.create_task(self.udpflusher())

	def set_dmetcp_con(self, dmetcp_con):
		self._dmetcp_connection = dmetcp_con

	def set_dmeudp_con(self, dmeudp_con):
		self._dmeudp_connection = dmeudp_con

	def send_dmetcp(self, data: bytes):
		self._dmetcp_connection.writer.write(data)

	def send_dmeudp(self, data: bytes):
		self._dmeudp_queue.put(data)

	async def tcpflusher(self):
	    while True:
	        await asyncio.sleep(self._dmetcp_aggtime)
	        await self._dmetcp_connection.writer.drain()

	async def udpflusher(self):
	    while True:
	    	size = self._dmeudp_queue.qsize()
	    	
	    	for i in range(size):
	       		data = self._dmeudp_queue.get()
	       		self._dmeudp_connection.send(data)
	    	await asyncio.sleep(self._dmeudp_aggtime)

	def deframe(self, connection, data: [bytes]):
		'''
		We have to deframe within the connection, as packet fragmentation will occur and we need to save incomplete packets
		'''
		if connection.server_name == 'mls':
			return self._mls_deframe_buffer.deframe(data)
		elif connection.server_name == 'dmetcp':
			return self._dmetcp_deframe_buffer.deframe(data)
		elif connection.server_name == 'dmeudp':
			return self._dmeudp_deframe_buffer.deframe(data)

	def get_mls_world_id(self) -> int:
		return self._mls_world_id

	def set_mls_world_id(self, mls_world_id: int) -> None:
		self._mls_world_id = mls_world_id

	def get_account_id(self):
		return self._account_id

	def get_username(self):
		return self._username

	def get_dme_world_id(self) -> int:
		if self._game == None:
			return 0
		return self._game.get_dme_world_id()

	def get_player_status(self) -> MediusPlayerStatus:
		return self._status

	def set_game(self, game):
		self._game = game

	def get_game(self):
		return self._game

	def close(self):
		if self._dmetcp_flush_task != None:
			self._dmetcp_flush_task.cancel()
		if self._dmeudp_flush_task != None:
			self._dmeudp_flush_task.cancel()

	def __str__(self):
		return f'Player(account_id={self._account_id},username={self._username},status={self._status},mls_world_id={self._mls_world_id},dme={self._game})'

	def get_dmetcp_ip(self):
		return self._dmetcp_connection.addr
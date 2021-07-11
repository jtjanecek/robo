import threading
import random
from enums.enums import MediusEnum, MediusPlayerStatus, MediusWorldStatus
from infra.sqllitedb import SqlLiteDb
from infra.game import Game
from infra.connection import UdpConnection, Connection
from infra.player import Player

class ClientManager:
	def __init__(self):
		self._db = SqlLiteDb()

		# Used in Mas only
		self._new_session_keys = set()
		self._new_session_keys_lock = threading.Lock()

		self._access_keys = set()
		self._access_keys_lock = threading.Lock()

		# ======================================================
		# Account id -> Player
		# Master list
		self._players = {}

		# Connection -> Player for fast access
		self._mls_cons = {}
		self._dmetcp_cons = {}
		self._dmeudp_cons = {}

		# dme world id -> gameworld
		self._ongoing_game_id = 1
		self._games = {}
		self._games_lock = threading.Lock()

	def identify(self, connection):
		if connection.server_name == 'mas':
			return None
		elif connection.server_name == 'mls':
			if connection in self._mls_cons.keys():
				return self._mls_cons[connection]
		elif connection.server_name == 'dmetcp':
			if connection in self._dmetcp_cons.keys():
				return self._dmetcp_cons[connection]
		elif connection.server_name == 'dmeudp':
			if connection.hash() in self._dmeudp_cons.keys():
				return self._dmeudp_cons[connection.hash()]
		else:
			return None

	# =============== Connection methods ===============
	def mls_connected(self, mls_con, session_key: bytes, target_world_id: int) -> bool:
		# Get the account id of the user who connected
		account_id = self._db.get_account_id(session_key = session_key)
		username = self._db.get_username(session_key = session_key)

		if account_id == None:
			return None

		# Check if that user is already logged in
		logged_in = account_id in self._players.keys()

		if not logged_in:
			self._players[account_id] = Player(account_id, username, session_key, target_world_id, mls_con)
			self._mls_cons[mls_con] = self._players[account_id]
		else:
			raise Exception("User is already logged in!")

		return True

	def dmetcp_connected(self, con, session_key: bytes, dme_world_id: int) -> bool:		
		# Get the account id of the user who connected
		account_id = self._db.get_account_id(session_key = session_key)

		if (account_id == None):
			return False

		player = self._players[account_id]
		self._dmetcp_cons[con] = player

		# update the game
		self._games[dme_world_id].player_tcp_connected(player, con)

		return True

	def dmeudp_connected(self, con: UdpConnection, serialized: dict) -> bool:		
		# Get the account id of the user who connected
		dme_player_id = serialized['dme_player_id']
		dme_world_id = serialized['dme_world_id']

		dme_game = self._games[dme_world_id]

		dme_game.player_udp_connected(dme_player_id, con)

		player = dme_game.get_player_by_dme_player_id(dme_player_id)

		self._dmeudp_cons[con.hash()] = player


	def client_disconnected(self, con):
		if con.server_name not in ['mls', 'dmetcp']:
			return

		if con.server_name == 'mls':
			# Delete this player from mls
			if con in self._mls_cons.keys():
				account_id = self._mls_cons[con].get_account_id()
				del self._mls_cons[con]
				self._players[account_id].close()
				del self._players[account_id]

		elif con.server_name == 'dmetcp':
			if con in self._dmetcp_cons.keys():
				player = self._dmetcp_cons[con]

				player.get_game().player_disconnected(player)

				del self._dmetcp_cons[con]
				del self._dmeudp_cons[player._dmeudp_connection]

	def dmetcp_broadcast(self, con: Connection, data: bytes):
		source_player = self._dmetcp_cons[con]
		game = source_player.get_game()
		game.dmetcp_broadcast(source_player, data)

	def dmeudp_broadcast(self, con: UdpConnection, data: bytes):
		source_player = self._dmeudp_cons[con.hash()]
		game = source_player.get_game()
		game.dmeudp_broadcast(source_player, data)

	# =============== Dme ===============
	def create_game(self, create_game_serialized: dict):
		with self._games_lock:
			new_dme_world_id = self._ongoing_game_id
			self._ongoing_game_id += 1

			# Actually create the game
			self._games[new_dme_world_id] = Game(new_dme_world_id, create_game_serialized)

			return new_dme_world_id

	def get_dme_world_player_count(self, dme_world_id: int):
		return self._games[dme_world_id].get_player_count()

	def get_game_status(self, dme_world_id: int):
		if dme_world_id not in self._games.keys():
			return MediusWorldStatus.WORLD_CLOSED
		return self._games[dme_world_id].get_game_status()

	def get_games(self): 
		return list(self._games.values())

	def get_game(self, dme_world_id):
		if dme_world_id in self._games.keys():
			return self._games[dme_world_id]
		return None

	# MLS Call
	def get_players_by_world(self, world_id: int):
		players = []
		for player in self._players.values():
			if player.get_mls_world_id() == world_id:
				players.append({
					'account_id': player.get_account_id(),
					'username': player.get_username(), 
					'mls_world_id': player.get_mls_world_id(), 
					'dme_world_id': player.get_dme_world_id(),
					'player_status': player.get_player_status()
				})
		return players

	def get_player(self, account_id: int) -> Player:
		return self._players[account_id]

	def get_player_from_mls_con(self, con):
		return self._mls_cons[con]

	# =============== DB Access Methods ===============

	def get_account_id(self, username=None, session_key=None):
		return self._db.get_account_id(username=username, session_key=session_key)

	def get_account_type(self, account_id: int):
		return self._db.get_account_type(account_id)

	def get_username(self, account_id=None, session_key=None):
		return self._db.get_username(account_id=account_id, session_key=session_key)

	def get_player_status(self, account_id):
		if account_id not in self._players.keys():
			return MediusPlayerStatus.MEDIUS_PLAYER_DISCONNECTED
		return self._players[account_id].get_player_status()

	def get_player_stats(self, account_id: int):
		return self._db.get_stats(account_id)

	def update_player_stats(self, account_id, stats: str):
		self._db.update_stats(account_id, stats)

	def get_player_ladderstatswide(self, account_id: int):
		return self._db.get_ladderstatswide(account_id)

	def update_player_ladderstatswide(self, account_id, ladderstatswide: str):
		self._db.update_ladderstatswide(account_id, ladderstatswide)

	# =============== Misc ===============

	def generate_access_key(self) -> bytes:
		new_access_key = ''.join(random.choice('0123456789ABCDEF') for i in range(MediusEnum.ACCESSKEY_MAXLEN-1)) + '\0'
		new_access_key = new_access_key.encode()

		with self._access_keys_lock:
			self._access_keys.add(new_access_key)
		return new_access_key

	def validate_access_key(self, access_key: bytes) -> bool:
		with self._access_keys_lock:
			access_key_valid = access_key in self._access_keys
			if access_key_valid:
				self._access_keys.remove(access_key)
		return access_key_valid

	def generate_session_key(self) -> bytes:
		new_session_key = ''.join(random.choice('0123456789ABCDEF') for i in range(MediusEnum.SESSIONKEY_MAXLEN-1)) + '\0'
		new_session_key = new_session_key.encode()

		with self._new_session_keys_lock:
			self._new_session_keys.add(new_session_key)
		return new_session_key

	def account_login(self, username: str, password: str, session_key: bytes):
		with self._new_session_keys_lock:
			session_key_valid = session_key in self._new_session_keys
			if session_key_valid:
				self._new_session_keys.remove(session_key)

		login_success = self._db.check_login(username, password, session_key)
		return login_success

	def __str__(self):
		result = '========================== Client Manager =========================='
		for player in self._players.values():
			result += '\n' + str(player)
		return result
import threading
import random
import boto3
from datetime import datetime
import json

from enums.enums import MediusEnum, MediusPlayerStatus, MediusWorldStatus, CLANTAG_ALLOWED_CHARACTERS
from infra.sqllitedb import SqlLiteDb
from infra.game import Game
from infra.connection import UdpConnection, Connection
from infra.player import Player
from utils import utils
from api.parser import get_clean_clan_tag_from_stats


import logging
logger = logging.getLogger("robo.clientmanager")

class ClientManager:
    def __init__(self, config):
        self._db = SqlLiteDb(db_loc=config['log_location'], salt=config['bcrypt_salt'])

        self._config = config

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

        # ======================================================
        self._channels = config['channels']




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
            ladderstatswide = self.get_player_ladderstatswide(account_id)
            self._players[account_id] = Player(account_id, username, session_key, target_world_id, mls_con, ladderstatswide)
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

        username = self._db.get_username(account_id)
        if username[0:3].lower() == 'cpu':
            self._games[dme_world_id].cpu_game()

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
                # Shut down dme coroutines if they exist
                self._players[account_id].close()
                del self._players[account_id]

        elif con.server_name == 'dmetcp':
            if con in self._dmetcp_cons.keys():
                player = self._dmetcp_cons[con]

                game = player.get_game()
                game.player_disconnected(player)

                if game.get_player_count() == 0:
                    logger.info(f"Game destroyed: {game.to_json()}!")
                    # Destroy the game
                    dme_world_game_id = game.get_dme_world_id()
                    del self._games[dme_world_game_id]

                player.set_game(None)
                player.set_player_status(MediusPlayerStatus.MEDIUS_PLAYER_IN_CHAT_WORLD)

                # Delete this players dme connections
                del self._dmetcp_cons[con]
                del self._dmeudp_cons[player._dmeudp_connection.hash()]

    def dmetcp_broadcast(self, con: Connection, data: bytes):
        source_player = self._dmetcp_cons[con]
        game = source_player.get_game()
        game.dmetcp_broadcast(source_player, data)

    def dmeudp_broadcast(self, con: UdpConnection, data: bytes):
        source_player = self._dmeudp_cons[con.hash()]
        game = source_player.get_game()
        game.dmeudp_broadcast(source_player, data)

    # =============== Dme ===============
    def create_game(self, create_game_serialized: dict, dmetcp_aggtime, dmeudp_aggtime):
        with self._games_lock:
            new_dme_world_id = self._ongoing_game_id
            self._ongoing_game_id += 1

            # Actually create the game
            self._games[new_dme_world_id] = Game(new_dme_world_id, create_game_serialized, dmetcp_aggtime, dmeudp_aggtime)

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
        result = []
        for player in self._players.values():
            if player.get_mls_world_id() == world_id:
                result.append(player)
        return result

    def get_player(self, account_id: int) -> Player:
        if account_id not in self._players.keys():
            return None
        return self._players[account_id]

    def get_player_from_mls_con(self, con):
        return self._mls_cons[con]

    # =============== DB Access Methods ===============

    def register_ip(self, username, ip):
        logger.info(f"User IP logged: {username} {ip}")
        self._db.register_ip(username, ip)

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

    def create_clan(self, clan_name: bytes, player_account_id: int, player_username: str):
        return self._db.create_clan(clan_name, player_account_id, player_username)

    def get_clan_id_from_account_id(self, account_id: int):
        return self._db.get_clan_id_from_account_id(account_id)

    def get_clan_id_from_name(self, clan_name):
        return self._db.get_clan_id_from_name(clan_name)

    def get_clan_info(self, clan_id: int):
        return self._db.get_clan_info(clan_id)

    def update_clan_stats(self, clan_id: int, stats: str):
        return self._db.update_clan_stats(clan_id, stats)

    def update_clan_message(self, clan_id: int, clan_message: str):
        return self._db.update_clan_message(clan_id, clan_message)

    def get_clan_message(self, clan_id: int):
        return self._db.get_clan_message(clan_id)

    def get_clan_member_account_ids(self, clan_id: int):
        return self._db.get_clan_member_account_ids(clan_id)

    def get_clan_invitations_sent(self, clan_id: int):
        return self._db.get_clan_invitations_sent(clan_id)

    def get_clan_statswide(self, clan_id: int):
        return self._db.get_clan_statswide(clan_id)

    def update_clan_statswide(self, clan_id: int, statswide: str):
        return self._db.update_clan_statswide(clan_id, statswide)

    def invite_player_to_clan(self, account_id: int, clan_id: int, invite_message: str):
        return self._db.invite_player_to_clan(account_id, clan_id, invite_message)

    def get_clan_invitations(self, account_id: int):
        return self._db.get_clan_invitations(account_id)

    def get_clan_leader_account_id(self, clan_id: int):
        return self._db.get_clan_leader_account_id(clan_id)

    def get_clan_name(self, clan_id: int):
        return self._db.get_clan_name(clan_id)

    def get_clan_name_from_account_id(self, account_id: int):
        clan_id = self.get_clan_id_from_account_id(account_id)
        if clan_id == None:
            return ''
        clan_name = self.get_clan_name(clan_id)
        return clan_name

    def get_clan_tag_from_account_id(self, account_id: int):
        clan_id = self.get_clan_id_from_account_id(account_id)
        if clan_id == None:
            return ''

        clan_info = self.get_clan_info(clan_id)

        tag = get_clean_clan_tag_from_stats(clan_info['clan_stats'])

        return tag

    def respond_clan_invite(self, clan_invitation_id, accepted):
        return self._db.respond_clan_invite(clan_invitation_id, accepted)

    def remove_clan_invite(self, clan_id, account_id):
        return self._db.remove_clan_invite(clan_id, account_id)

    def disband_clan(self, clan_id: int):
        return self._db.disband_clan(clan_id)

    def remove_player_from_clan(self, account_id: int, clan_id: int):
        return self._db.remove_player_from_clan(account_id, clan_id)

    def transfer_clan_ownership(self, clan_id: int, new_account_id: int, new_account_name: str):
        return self._db.transfer_clan_ownership(clan_id, new_account_id, new_account_name)

    def add_buddy(self, account_id: int, buddy_id: int):
        return self._db.add_buddy(account_id, buddy_id)

    def get_buddies(self, account_id: int):
        return self._db.get_buddies(account_id)

    def remove_buddy(self, account_id, buddy_id):
        return self._db.remove_buddy(account_id, buddy_id)

    def delete_user(self, session_key: str, password: str):
        self._db.delete_user(session_key, password)


    # =============== Clans ===============
    def create_channel(self, serialized_channel):
        clan_id = serialized_channel['generic_field_1']
        channel = self.get_channel_by_clan_id(clan_id)
        if channel != None:
            return channel['id']

        # Have to add it
        serialized_channel['id'] = self.get_new_channel_id()
        self._channels.append(serialized_channel)
        return serialized_channel['id']

    def get_channel_by_clan_id(self, clan_id):
        for channel in self._channels:
            if channel['generic_field_1'] == clan_id:
                return channel
        return None

    def get_new_channel_id(self):
        max_id = max([channel['id'] for channel in self._channels])
        return max_id+1

    def get_channels(self) -> list:
        return self._channels

    # =============== Misc ===============

    def api_req_players(self) -> list:
        result = [player.to_json() for player in self._players.values()]
        for player_dict in result:
            player_dict['stats'] = self.get_player_stats(player_dict['account_id'])
            player_dict['ladderstatswide'] = self.get_player_ladderstatswide(player_dict['account_id'])
        return result

    def api_req_games(self) -> list:
        result = [game.to_json() for game in self._games.values()]
        return result

    def api_check_alts(self, username):
        return self._db.check_alts(username)

    # new ones
    def api_req_account_id(self, account_id):
        return self._db.get_all_user_info_from_account_id(account_id)

    def api_req_username(self, username):
        return self._db.get_all_user_info_from_username(username)

    def api_req_clan_id(self, clan_id):
        data = self._db.get_clan_info(clan_id)
        if data != {}:
            account_ids = self._db.get_clan_member_account_ids(clan_id)
            data['members'] = []
            for account_id in account_ids:
                data['members'].append(self._db.get_username(account_id=account_id))
        return data

    def api_req_clan_name(self, clan_name):
        data = self._db.get_clan_info_from_name(clan_name)
        if data != {}:
            account_ids = self._db.get_clan_member_account_ids(data['clan_id'])
            data['members'] = []
            for account_id in account_ids:
                data['members'].append(self._db.get_username(account_id=account_id))
        return data

    def clear_zombie_games(self):
        for dme_world_id in list(self._games.keys()):
            game = self._games[dme_world_id]
            if datetime.now().timestamp() - game.get_created_date() > 10 and game.get_player_count() == 0:
                # Delete this game
                del self._games[dme_world_id]

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
        username_valid = utils.check_username_valid(username)
        if username_valid == False:
            return False

        with self._new_session_keys_lock:
            session_key_valid = session_key in self._new_session_keys
            if session_key_valid:
                self._new_session_keys.remove(session_key)

        login_success = self._db.check_login(username, password, session_key)

        return login_success

    def trigger_cpu(self, player, cpu_type):
        if self._config['cpus']['enabled'] != 'True':
            return

        cpu_type_translation = {
            'cpu0': 'bot0',
            'cpu1': 'bot1',
            'cpu2': 'bot2',
            'cpu3': 'bot3',
            'cpu4': 'bot4',
            'cpug': 'botg'
        }

        bolt_translation = {
            'cpu0': 1,
            'cpu1': 1,
            'cpu2': 2,
            'cpu3': 3,
            'cpu4': 4,
            'cpug': 4
        }

        if cpu_type not in cpu_type_translation.keys():
            return

        logger.info(f"Triggering lambda: cpu_type: {cpu_type}")

        game = player.get_game()
        if game == None:
            return

        if game.get_player_by_dme_player_id(0) != player:
            return

        # Get dme world id
        world_id = game.get_dme_world_id()
        # first, check if the player is a host of a game

        session = boto3.session.Session(aws_access_key_id=self._config['cpus']['aws_access_key_id'],aws_secret_access_key=self._config['cpus']['aws_secret_access_key'],region_name=self._config['cpus']['region_name'])
        lambda_client = session.client('lambda')

        # Get the following for the CPU:
        # - account id
        # - username
        # - session_key
        # While this CPU is not online
        username = f"CPU-{str(int(random.random() * 997) + 1).zfill(3)}"
        account_id = self._db.get_account_id(username)
        while account_id in self._players.keys():
            username = f"CPU-{str(int(random.random() * 997) + 1).zfill(3)}"
            account_id = self._db.get_account_id(username)

        logger.info(f"CPU username/account id: {username} | {account_id}")

        session_key = self._db.get_session_key(account_id).strip("\x00")

        logger.info(f"Using: {username}")

        config = {
            "bot_class": cpu_type_translation[cpu_type],
            "account_id": account_id,
            "username": username,
            "world_id": world_id,
            "skin": "random",
            "bolt": bolt_translation[cpu_type],
            "clan_tag": "",
            "team": "blue",
            "autojoin": "False",
            "session_key": session_key,
            "mls_ip": self._config['public_ip'],
            "mls_port": self._config['mls']['port'],
            "dmetcp_ip": self._config['public_ip'],
            "dmetcp_port": self._config['dmetcp']['port'],
            "dmeudp_ip": self._config['public_ip'],
            "dmeudp_port": self._config['dmeudp']['port']
        }
        config = json.dumps(config)
        logger.info(f"Invoking ... {config}")
        lambda_client.invoke(FunctionName=self._config['cpus']['function_name'], Payload=config, InvocationType='Event')
        logger.info("Started.")

    def __str__(self):
        result = '========================== Client Manager =========================='
        for player in self._players.values():
            result += '\n' + str(player)
        return result

    def dump_stats(self):
        return self._db.dump_stats()

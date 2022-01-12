from copy import deepcopy
from enums.enums import MediusWorldStatus, MediusEnum, RtIdEnum, MediusPlayerStatus
from utils import utils
from medius.rtpackets.serverconnectnotify import ServerConnectNotifySerializer
from medius.rtpackets.clientappsingle import ClientAppSingleSerializer
from medius.rtpackets.serverdisconnectnotify import ServerDisconnectNotifySerializer
import base64
from datetime import datetime

import logging
logger = logging.getLogger('robo.game')


class Game:
    def __init__(self, dme_world_id: int, create_game_serialized: dict, dmetcp_aggtime, dmeudp_aggtime):
        self._status = MediusWorldStatus.WORLD_PENDING_CREATION
        self._dme_world_id = dme_world_id
        self._create_game_serialized = create_game_serialized
        self._dmetcp_aggtime = dmetcp_aggtime
        self._dmeudp_aggtime = dmeudp_aggtime

        self._stats = utils.hex_to_bytes(''.join(['00'] * MediusEnum.GAMESTATS_MAXLEN))

        self._created_date = datetime.now().timestamp()
        self._started_date = ''

        self._possible_dme_player_ids = {0,1,2,3,4,5,6,7}
        # Dict for dme player id -> Player
        self._players = {}

    def active(self):
        if self._status != MediusWorldStatus.WORLD_ACTIVE:

            logger.info(f"Game {self.to_json()} started!")

            self._status = MediusWorldStatus.WORLD_ACTIVE
            game_name = self._create_game_serialized['game_name'].decode()
            game_name = f"[IG] {game_name}"
            self._create_game_serialized['game_name'] = game_name[0:MediusEnum.GAMENAME_MAXLEN].encode()
            self._started_date = datetime.now().timestamp()

            for player in self._players.values():
                player.set_player_status(MediusPlayerStatus.MEDIUS_PLAYER_IN_GAME_WORLD)
                player.set_dmetcp_aggtime(self._dmetcp_aggtime)
                player.set_dmeudp_aggtime(self._dmeudp_aggtime)

    def get_mls_world_id(self):
        return self._create_game_serialized['game_level']

    def get_game_status(self) -> MediusWorldStatus:
        return self._status

    def player_tcp_connected(self, player, dmetcp_con) -> None:
        '''A player has just connected to this dme world via tcp.

        1. Generate a new dme player id for this player.
        2. Add this connection to the player list
        3. Set this game in the dmetcp connection
        4. Start the tcpflusher coroutine

        '''

        if len(self._players) == 8 or self._status == MediusWorldStatus.WORLD_ACTIVE:
            logger.warning(f'Attempt to join full or active game!')

        dme_player_id = self._generate_new_dme_player_id()
        self._players[dme_player_id] = player

        player.set_dmetcp_con(dmetcp_con)
        # Set the game to be referenced by this player
        player.set_game(self)
        # Start the TCP flush coroutine
        player.start_tcpflusher()

        self._status = MediusWorldStatus.WORLD_STAGING

    def player_udp_connected(self, dme_player_id: int, udp_con) -> None:
        player = self._players[dme_player_id]
        player.set_dmeudp_con(udp_con)
        # Start the UDP flush coroutine
        player.start_udpflusher()

    def send_server_notify_connected(self, player):
        dme_player_id = self.get_dme_player_id(player)
        ip = player.get_dmetcp_ip()

        packet = utils.rtpacket_to_bytes(ServerConnectNotifySerializer.build(dme_player_id, ip))
        logger.info(f"PACKET SERVER NOTIFY: {utils.bytes_to_hex(packet)}")

        for dest_player in self._players.values():
            if dest_player != player:
                # send server notify 
                dest_player.send_dmetcp(packet)

    def send_server_notify_disconnected(self, player):
        dme_player_id = self.get_dme_player_id(player)
        ip = player.get_dmetcp_ip()
        packet = utils.rtpacket_to_bytes(ServerDisconnectNotifySerializer.build(dme_player_id, ip))
        logger.info(f"PACKET SERVER NOTIFY: {utils.bytes_to_hex(packet)}")

        for dest_player in self._players.values():
            if dest_player != player:
                # send server notify 
                dest_player.send_dmetcp(packet)

    def dmetcp_single(self, player, data: bytes):
        data = bytearray(data)
        target_player_id = data[0]

        # Change the source to be that player
        data[0] = self.get_dme_player_id(player)

        data = bytes(data)

        packet_data = utils.rtpacket_to_bytes(ClientAppSingleSerializer.build(data))

        try:
            self._players[target_player_id].send_dmetcp(bytes(packet_data))
        except KeyError:
            logger.debug("Tried to send to non-existant player!")

    def dmeudp_single(self, player, data: bytes):
        data = bytearray(data)
        target_player_id = data[0]

        # Change the source to be that player
        data[0] = self.get_dme_player_id(player)

        packet_data = utils.rtpacket_to_bytes(ClientAppSingleSerializer.build(data))

        try:
            self._players[target_player_id].send_dmeudp(bytes(packet_data))
        except KeyError:
            logger.debug("Tried to send to non-existant player!")

    def player_disconnected(self, player):
        player.close()
        dme_player_id = self.get_dme_player_id(player)
        self.send_server_notify_disconnected(player)
        del self._players[dme_player_id]

    def _generate_new_dme_player_id(self):
        return min(self._possible_dme_player_ids.difference(set(self._players.keys())))

    def get_player_count(self) -> int:
        return len(self._players)

    def get_dme_world_id(self):
        return self._dme_world_id

    def get_dme_player_id(self, player):
        for dme_player_id, p in self._players.items():
            if player == p:
                return dme_player_id

    def get_player_by_dme_player_id(self, dme_player_id):
        return self._players[dme_player_id]

    def dmetcp_broadcast(self, player, data: bytes):
        source_dme_player_id = self.get_dme_player_id(player)

        packet = utils.format_rt_message(RtIdEnum.CLIENT_APP_SINGLE, utils.int_to_bytes_little(2,source_dme_player_id), data)

        for dest_player in self._players.values():
            if dest_player != player:
                dest_player.send_dmetcp(packet)

    def dmeudp_broadcast(self, player, data: bytes):
        source_dme_player_id = self.get_dme_player_id(player)

        packet = utils.format_rt_message(RtIdEnum.CLIENT_APP_SINGLE, utils.int_to_bytes_little(2, source_dme_player_id), data)

        for dest_player in self._players.values():
            if dest_player != player:
                dest_player.send_dmeudp(packet)

    def get_created_date(self):
        return self._created_date

    def get_created_info(self):
        return self._create_game_serialized

    def get_stats(self):
        return self._stats

    def set_stats(self, stats):
        self._stats = stats

    def get_players(self):
        res = []
        for player in self._players.values():
            res.append({
                'account_id': player.get_account_id(),
                'username': player.get_username()
            })
        return res

    def to_json(self) -> dict:
        game_data = deepcopy(self._create_game_serialized)
        result = {
            'created_date': self._created_date,
            'started_date': self._started_date,
            'status': self._status,
            'dme_world_id': self._dme_world_id,
            'min_players': game_data['min_players'],
            'max_players': game_data['max_players'],
            'game_level': game_data['game_level'],
            'game_name': base64.b64encode(game_data['game_name']).decode(),
            'player_skill_level': game_data['player_skill_level'],
            'rules_set': game_data['rules_set'],
            'generic_field_1': game_data['generic_field_1'],
            'generic_field_2': game_data['generic_field_2'],
            'generic_field_3': game_data['generic_field_3'],
            'game_host_type': game_data['game_host_type'],
            'dmetcp_aggtime': self._dmetcp_aggtime,
            'dmeudp_aggtime': self._dmeudp_aggtime,
            'players': [player.to_json() for player in self._players.values()]
        }
        return result

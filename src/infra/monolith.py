import asyncio
import logging

from enums.enums import CipherContext
from crypto.rsa import RSA
from enums.rtid import RtId
from enums.enums import RtIdEnum
from utils import utils
from infra.clientmanager import ClientManager
from infra.connection import Connection
from infra.chatcommands import ChatCommands
from infra.patch import PatchManager
from crypto.rsa import RSA
from utils.rtbufferdeframer import RtBufferDeframer
from enums.enums import MediusChatMessageType

import queue
from datetime import datetime


class Monolith:

    def __init__(self, config: dict):
        self._config = config
        self._client_manager = ClientManager(config)
        self._chat_commands = ChatCommands()
        self._logger = logging.getLogger('robo.monolith')
        self._patch_manager = PatchManager(self._config)

        self._chat_messages = queue.Queue()

        self._leaderboards = None
        self._clan_leaderboards = None

    #################################################################################
    # UDP Pipeline
    #################################################################################

    def process_udp(self, con, data, logger):
        if con.server_name == 'nat':
            # We don't need nat yet
            if len(data) == 4 and data[-1] != 0xd4:
                if con.addr[0:3] == '192': # Local address. Debugging purposes
                    ip_formatted = bytes([0] * 4)
                else:
                    ip_formatted = bytes([int(y) for y in con.addr.split('.')])
                port = utils.int_to_bytes_little(2, con.port)
                con.send(ip_formatted + port)
            return []
        # This means its dmeudp.
        # We need to tie this to a tcp connection to deframe if it's > 100 bytes

        player = self._client_manager.identify(con)

        ###### DEFRAME
        # Player has been identified
        if player != None:
            packets = player.deframe(con, data)
            # for packet in packets:
            #     logger.debug(f"{player} | Deframe | {utils.bytes_to_hex(packet)}")
        else: # Player has not been identified
            packets = RtBufferDeframer.basic_deframe(data)

        ## SERIALIZE
        serialized = [self._serialize(packetBytes) for packetBytes in packets]
        for serial in serialized:
            logger.debug(f"{con} | Serialized | {serial}")

        for packet in serialized:
            if packet['packet'] == 'medius.rtpackets.clientappsingle':
                try:
                    this_pkt = {'type':'udp'}
                    this_pkt['dme_world_id'] = player.get_game().get_dme_world_id()
                    this_pkt['src'] = player.get_game().get_dme_player_id(player)
                    this_pkt['dst'] = utils.bytes_to_int_little(packet['data'][0:2])
                    this_pkt['data'] = utils.bytes_to_hex(packet['data'][2:])
                    self._api._dme_queue.put(this_pkt)
                except Exception:
                    logger.exception()
            elif packet['packet'] == 'medius.rtpackets.clientappbroadcast':
                try:
                    this_pkt = {'type':'udp'}
                    this_pkt['dme_world_id'] = player.get_game().get_dme_world_id()
                    this_pkt['src'] = player.get_game().get_dme_player_id(player)
                    this_pkt['dst'] = -1
                    this_pkt['data'] = utils.bytes_to_hex(packet['data'])
                    self._api._dme_queue.put(this_pkt)
                except Exception:
                    logger.exception()

        ## RESPONSE
        responses = utils.flatten([self._rtresponse(con, packetBytes) for packetBytes in serialized])
        for response in responses:
            logger.debug(f"{con} | Response | {response}")

        ## TO BYTES
        responses = [utils.rtpacket_to_bytes(packet) for packet in responses]
        # for response in responses:
        #     logger.debug(f"{con} | Encrypted | {utils.bytes_to_hex(response)}")

        return responses

    #################################################################################
    # TCP Pipeline
    #################################################################################

    def process_tcp(self, con: Connection, data: bytes, logger):
        # Identify the player -- if the player is not identified, then run anonymous pipeline
        player = self._client_manager.identify(con)

        ###### DEFRAME
        # Player has been identified
        if player != None:
            packets = player.deframe(con, data)
            for packet in packets:
                logger.debug(f"{player} | Deframe | {utils.bytes_to_hex(packet)}")
        else: # Player has not been identified
            packets = RtBufferDeframer.basic_deframe(data)

        ###### DECRYPT
        # We only need to decrypt in mas
        if con.server_name == 'mas':
            packets = [self._decrypt(con, packet) for packet in packets]
            #for decrypt in decrypted:
            #    logger.debug(f"{con} | Decrypted | {utils.bytes_to_hex(decrypt)}")

        ## SERIALIZE
        packets = [self._serialize(packet) for packet in packets]
        for serial in packets:
            logger.debug(f"{con} | Serialized | {serial}")

        for packet in packets:
            if packet['packet'] == 'medius.rtpackets.clientappsingle':
                try:
                    this_pkt = {'type':'tcp'}
                    this_pkt['dme_world_id'] = 0
                    this_pkt['src'] = player.get_game().get_dme_world_id()
                    this_pkt['dst'] = utils.bytes_to_int_little(packet['data'][0:2])
                    this_pkt['data'] = utils.bytes_to_hex(packet['data'][2:])
                    self._api._dme_queue.put(this_pkt)
                except Exception:
                    logger.exception()
            elif packet['packet'] == 'medius.rtpackets.clientappbroadcast':
                try:
                    this_pkt = {'type':'tcp'}
                    this_pkt['dme_world_id'] = player.get_game().get_dme_world_id()
                    this_pkt['src'] = player.get_game().get_dme_player_id(player)
                    this_pkt['dst'] = -1
                    this_pkt['data'] = utils.bytes_to_hex(packet['data'])
                    self._api._dme_queue.put(this_pkt)
                except Exception:
                    logger.exception()

        ## RESPONSE
        responses = utils.flatten([self._rtresponse(con, packetBytes) for packetBytes in packets])
        for response in responses:
            logger.debug(f"{con} | Response | {response}")

        ## ENCRYPT
        encrypted = [self._encrypt(con, utils.rtpacket_to_bytes(packet)) for packet in responses]
        #for encrypt in encrypted:
        #    logger.debug(f"{con} | Encrypted | {utils.bytes_to_hex(encrypt)}")

        return encrypted

    def _decrypt(self, con: Connection, data: bytes) -> bytes:
        ''' If we are on MAS, decrypt the data. Otherwise, just pass it along
        '''
        # Leave only mas encrypted
        if con.server_name not in ['mls', 'mas']:
            return data

        # Data is unencrypted
        if data[0] < 0x80:
            return data

        rtid = data[0] & 0x7F
        rtlen = data[1:3]
        rthash = data[3:7]
        remaining_data = data[7:]

        hashctx = rthash[3] & 0xFF
        hashctx = hashctx >> 0x05

        if hashctx == CipherContext.RSA_AUTH:
            return bytes([rtid] + [b for b in rtlen] + list(RSA().decrypt(remaining_data, rthash)))
        elif hashctx == CipherContext.RC_CLIENT_SESSION:
            decrypted_bytes =  con.get_rc4().decrypt(remaining_data, rthash)
            return utils.format_rt_message(rtid, decrypted_bytes)
        elif hashctx == CipherContext.RC_SERVER_SESSION:
            decrypted_bytes =  con.get_server_rc4().decrypt(remaining_data, rthash)
            return utils.format_rt_message(rtid, decrypted_bytes)

    def _serialize(self, data: bytes) -> bytes:
        rt_info = RtId.map[data[0]]

        serialized = rt_info['serializer'].serialize(data)

        return serialized

    def _rtresponse(self, con: Connection, serialized) -> [bytes]:
        '''
        1. Serialize the data coming in into an RT/Medius type
        2. Get the response
        '''
        rt_info = RtId.map[serialized['rtid'][0]]

        responses = rt_info['handler'].process(serialized, self, con)

        return responses

    def _encrypt(self, con: Connection, data: bytes) -> [bytes]:
        '''
        If we are on mas, encrypt the data
        '''
        if con.server_name != 'mas':
            return data

        result = None
        if data[0] == RtIdEnum.SERVER_CRYPTKEY_PEER:
            result = con.get_rsa().encrypt(data)
        elif data[0] in [
                RtIdEnum.SERVER_CRYPTKEY_GAME,
                RtIdEnum.SERVER_CONNECT_ACCEPT_TCP,
                RtIdEnum.SERVER_CONNECT_COMPLETE,
                RtIdEnum.SERVER_APP,
                RtIdEnum.CLIENT_APP_TOSERVER
                ]:
            result = con.get_rc4().encrypt(data)

        if result == None:
            self._logger.warning("Data was not encrypted!")
            return data
        return result


# ===================================
# Client methods

    def get_client_manager(self):
        return self._client_manager

    def client_disconnected(self, con: Connection):
        self._client_manager.client_disconnected(con)

    def process_chat(self, player, text, chat_message_type):
        self._chat_commands.process_chat(player, text)

        if chat_message_type == MediusChatMessageType.BROADCAST:
            username = player.get_username()
            self._chat_messages.put({"username":username, "message":text, "ts": datetime.now().timestamp()})

    def process_login(self, player):
        self._patch_manager.process_login(player)

# ===================================
# API methods
    def api_req_players(self):
        return self._client_manager.api_req_players()

    def api_req_games(self):
        return self._client_manager.api_req_games()

    def api_req_chat(self) -> list:
        result = []
        size = self._chat_messages.qsize()
        for i in range(size):
            result.append(self._chat_messages.get())
        return result

    def api_req_check_alts(self, username):
        return self._client_manager.api_check_alts(username)

    def api_req_account_id(self, account_id):
        return self._client_manager.api_req_account_id(account_id)

    def api_req_username(self, username):
        return self._client_manager.api_req_username(username)

    def api_req_clan_id(self, clan_id):
        return self._client_manager.api_req_clan_id(clan_id)

    def api_req_clan_name(self, clan_name):
        return self._client_manager.api_req_clan_name(clan_name)

# ===================================
# Misc

    def clear_zombie_games(self):
        self._client_manager.clear_zombie_games()

    def get_mas_ip(self) -> str:
        return self._config['public_ip']

    def get_mas_port(self) -> int:
        return self._config['mas']['port']

    def get_mls_ip(self) -> str:
        return self._config['public_ip']

    def get_mls_port(self) -> int:
        return self._config['mls']['port']

    def get_dmetcp_ip(self) -> str:
        return self._config['public_ip']

    def get_dmetcp_port(self) -> int:
        return self._config['dmetcp']['port']

    def get_dmeudp_ip(self) -> str:
        return self._config['public_ip']

    def get_dmeudp_port(self) -> int:
        return self._config['dmeudp']['port']

    def get_nat_ip(self) -> str:
        return self._config['public_ip']

    def get_nat_port(self) -> int:
        return self._config['nat']['port']

    def get_app_id(self) -> int:
        return self._config['app_id']

    def get_locations(self) -> list:
        return self._config['locations']

    def get_policy(self) -> str:
        return self._config['policy']

    def get_announcement(self) -> str:
        return self._config['announcement']

    def update_leaderboards(self):
        self._leaderboards, self._clan_leaderboards = self._client_manager.dump_stats()

    def get_leaderboard_info(self, ladder_stat_index, sort_order, start_position, end_position):
        leaderboard = self._leaderboards[ladder_stat_index]
        if sort_order == 'DESC':
            # standard order
            return leaderboard[start_position-1:end_position-1]
        else:
            return leaderboard[start_position-1:end_position-1]

    def get_clan_leaderboard_info(self, ladder_stat_index, sort_order, start_position, end_position):
        leaderboard = self._clan_leaderboards[ladder_stat_index]
        if sort_order == 'DESC':
            # standard order
            return leaderboard[start_position-1:end_position-1]
        else:
            return leaderboard[start_position-1:end_position-1]

    def get_player_ranking(self, account_id, stat_index):
        leaderboard = self._leaderboards[stat_index]
        for i in range(len(leaderboard)):
            if leaderboard[i]['account_id'] == account_id:
                return i+1
        return self.get_total_rankings()

    def get_total_rankings(self):
        if self._leaderboards == None:
            return 9999
        return len(self._leaderboards[0])

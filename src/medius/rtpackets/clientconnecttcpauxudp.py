from enums.enums import MediusEnum
from utils import utils
from medius.rtpackets.serverconnectaccepttcp import ServerConnectAcceptTcpSerializer
from medius.rtpackets.serverinfoauxudp import ServerInfoAuxUdpSerializer

class ClientConnectTcpAuxUdpSerializer:
    data_dict = [
        {'name': 'rtid', 'n_bytes': 1, 'cast': None},
        {'name': 'len', 'n_bytes': 2, 'cast': utils.bytes_to_int_little},
        {'name': 'unknown1', 'n_bytes': 3, 'cast': None},
        {'name': 'target_world_id', 'n_bytes': 2, 'cast': utils.bytes_to_int_little},
        {'name': 'app_id', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
        {'name': 'key', 'n_bytes': 64, 'cast': utils.bytes_to_int_little},
        {'name': 'session_key', 'n_bytes': MediusEnum.SESSIONKEY_MAXLEN, 'cast': None},
        {'name': 'access_key', 'n_bytes': MediusEnum.ACCESSKEY_MAXLEN, 'cast': None}
    ]

    def serialize(self, data: bytes):
        return utils.serialize(data, self.data_dict, __name__)

class ClientConnectTcpAuxUdpHandler:
    def process(self, serialized, monolith, con):

        # Handle that a new user has connected
        client_manager = monolith.get_client_manager()
        
        # Check access key
        if not client_manager.validate_access_key(serialized['access_key']):
                raise Exception("Invalid access key")

        if client_manager.dmetcp_connected(con, serialized['session_key'], serialized['target_world_id']) == False:
            # No valid player found
            return []

        account_id = client_manager.get_account_id(session_key=serialized['session_key'])
        player = client_manager.get_player(account_id)
        dme_player_id = player.get_game().get_dme_player_id(player)
        num_players = player.get_game().get_player_count()

        packets = []
        packets.append(ServerConnectAcceptTcpSerializer.build(
            con.addr,
            dme_player_id = dme_player_id,
            player_count = num_players
        ))

        packets.append(ServerInfoAuxUdpSerializer.build(
            monolith.get_dmeudp_ip(),
            monolith.get_dmeudp_port()
        ))


        return packets
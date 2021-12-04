from enums.enums import RtIdEnum
from utils import utils

class ClientAppSingleSerializer:
    data_dict = [
        {'name': 'rtid', 'n_bytes': 1, 'cast': None},
        {'name': 'len', 'n_bytes': 2, 'cast': utils.bytes_to_int_little},
        {'name': 'data', 'n_bytes': None, 'cast': None}
    ]

    def serialize(self, data: bytes):
        return utils.serialize(data, self.data_dict, __name__)

    @classmethod
    def build(self, data: bytes):
        packet = [
            {'name': __name__},
            {'rtid': RtIdEnum.CLIENT_APP_SINGLE},
            {'data': data}
        ]
        return packet

class ClientAppSingleHandler:
    def process(self, serialized, monolith, con):

        player = monolith.get_client_manager().identify(con)

        game = player.get_game()
        if (con.server_name == 'dmetcp'):
            game.dmetcp_single(player, serialized['data'])
        else:
            game.dmeudp_single(player, serialized['data'])
            
        return []
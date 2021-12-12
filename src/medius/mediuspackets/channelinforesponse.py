from enums.enums import MediusIdEnum
from enums.enums import MediusEnum
from utils import utils

class ChannelInfoResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

    @classmethod
    def build(self,
            message_id: bytes,
            callback_status: int,
            lobby_name: str,
            active_player_count: int,
            max_players: int
            ):
        packet = [
            {'name': __name__},
            {'mediusid': MediusIdEnum.ChannelInfoResponse},
            {'message_id': message_id},
            {'buf': utils.hex_to_bytes("000000")},
            {'callback_status': utils.int_to_bytes_little(4, callback_status)},
            {'lobby_name': utils.str_to_bytes(lobby_name, MediusEnum.LOBBYNAME_MAXLEN)},
            {'active_player_count': utils.int_to_bytes_little(4, active_player_count)},
            {'max_players': utils.int_to_bytes_little(4, max_players)}
        ]
        return packet

class ChannelInfoResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: ChannelInfoResponseHandler')
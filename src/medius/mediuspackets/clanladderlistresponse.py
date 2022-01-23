from enums.enums import MediusIdEnum
from enums.enums import MediusEnum
from utils import utils

class ClanLadderListResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

    @classmethod
    def build(self,
            message_id,
            clan_id,
            clan_name,
            ladder_position,
            callback_status,
            end_of_list
            ):
        packet = [
            {'name': __name__},
            {'mediusid': MediusIdEnum.ClanLadderListResponse},
            {'message_id': message_id},
            {'buf': utils.hex_to_bytes("000000")},
            {'clan_id': utils.int_to_bytes_little(4, clan_id)},
            {'clan_name': utils.str_to_bytes(clan_name, MediusEnum.CLANNAME_MAXLEN)},
            {'ladder_position': utils.int_to_bytes_little(4, ladder_position)},
            {'callback_status': utils.int_to_bytes_little(4, callback_status)},
            {'end_of_list': utils.int_to_bytes_little(4, end_of_list)}
        ]
        return packet

class ClanLadderListResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: ClanLadderListResponseHandler')

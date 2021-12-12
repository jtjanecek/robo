from enums.enums import MediusIdEnum, MediusEnum
from utils import utils

class GetIgnoreListResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

    @classmethod
    def build(self,            
            message_id: bytes,
            callback_status: int,
            ignore_account_id: int,
            username: str,
            player_status: int,
            end_of_list: int
            ):
        packet = [
            {'name': __name__},
            {'mediusid': MediusIdEnum.GetIgnoreListResponse},
            {'message_id': message_id},
            {'buf': utils.hex_to_bytes("000000")},
            {'callback_status': utils.int_to_bytes_little(4, callback_status)},
            {'ignore_account_id': utils.int_to_bytes_little(4, ignore_account_id)},
            {'username': utils.str_to_bytes(username, MediusEnum.ACCOUNTNAME_MAXLEN)},
            {'player_status': utils.int_to_bytes_little(4, player_status)},
            {'end_of_list': utils.int_to_bytes_little(4, end_of_list)}
        ]
        return packet


class GetIgnoreListResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: GetIgnoreListResponseHandler')


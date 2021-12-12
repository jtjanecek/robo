from enums.enums import MediusIdEnum, MediusEnum
from utils import utils

class FindPlayerResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

    @classmethod
    def build(self,
            message_id: bytes,
            callback_status: int,
            app_id: int,
            app_name: str,
            app_type: int,
            world_id: int,
            account_id: int,
            account_name: str,
            end_of_list: int
            ):
        packet = [
            {'name': __name__},
            {'mediusid': MediusIdEnum.FindPlayerResponse},
            {'message_id': message_id},
            {'buf': utils.hex_to_bytes("000000")},
            {'callback_status': utils.int_to_bytes_little(4, callback_status, signed=True)},
            {'app_id': utils.int_to_bytes_little(4, app_id)},
            {'app_name': utils.str_to_bytes(app_name, MediusEnum.APPNAME_MAXLEN)},
            {'app_type': utils.int_to_bytes_little(4, app_type)},
            {'world_id': utils.int_to_bytes_little(4, world_id)},
            {'account_id': utils.int_to_bytes_little(4, account_id)},
            {'account_name': account_name},
            {'end_of_list': utils.int_to_bytes_little(4, end_of_list)}
        ]
        return packet


class FindPlayerResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: FindPlayerResponseHandler')
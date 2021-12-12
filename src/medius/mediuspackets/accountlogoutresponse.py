from enums.enums import MediusIdEnum
from enums.enums import MediusEnum
from utils import utils

class AccountLogoutResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

    @classmethod
    def build(self,
            message_id: bytes,
            callback_status: int
            ):
        packet = [
            {'name': __name__},
            {'mediusid': MediusIdEnum.AccountLogoutResponse},
            {'message_id': message_id},
            {'buf': utils.hex_to_bytes("000000")},
            {'callback_status': utils.int_to_bytes_little(4, callback_status)}
        ]
        return packet

class AccountLogoutResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: AccountLogoutResponseHandler')


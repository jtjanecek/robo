from enums.enums import MediusIdEnum
from utils import utils

class AccountGetIdResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

    @classmethod
    def build(self,
            message_id: bytes,
            account_id: int,
            callback_status: int
            ):
        packet = [
            {'name': __name__},
            {'mediusid': MediusIdEnum.AccountGetIdResponse},
            {'message_id': message_id},
            {'buf': utils.hex_to_bytes("000000")},
            {'account_id': utils.int_to_bytes_little(4, account_id)},
            {'callback_status': utils.int_to_bytes_little(4, callback_status, signed=True)}
        ]
        return packet

class AccountGetIdResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: AccountGetIdResponseHandler')


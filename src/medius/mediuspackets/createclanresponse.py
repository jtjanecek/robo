from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from enums.enums import MediusIdEnum

class CreateClanResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

    @classmethod
    def build(self,
            message_id,
            callback_status,
            clan_id
            ):
        packet = [
            {'name': __name__},
            {'mediusid': MediusIdEnum.CreateClanResponse},
            {'message_id': message_id},
            {'buf': utils.hex_to_bytes("000000")},
            {'callback_status': utils.int_to_bytes_little(4, callback_status, signed=True)},
            {'clan_id': utils.int_to_bytes_little(4, clan_id)}
        ]
        return packet

class CreateClanResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: CreateClanResponseHandler')


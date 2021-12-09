from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from enums.enums import MediusIdEnum


class RemovePlayerFromClanResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

    @classmethod
    def build(self,
            message_id,
            callback_status
        ):
        packet = [
            {'name': __name__},
            {'mediusid': MediusIdEnum.RemovePlayerFromClanResponse},
            {'message_id': message_id},
            {'buf': utils.bytes_from_hex("000000")},
            {'callback_status': utils.int_to_bytes_little(4, callback_status, signed=True)}
        ]
        return packet

class RemovePlayerFromClanResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: RemovePlayerFromClanResponseHandler')


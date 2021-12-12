from enums.enums import MediusIdEnum
from enums.enums import MediusEnum
from utils import utils

class CreateGameResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

    @classmethod
    def build(self,
            message_id: bytes,
            callback_status: int,
            new_dme_world_id: int):
        packet = [
            {'name': __name__},
            {'mediusid': MediusIdEnum.CreateGameResponse},
            {'message_id': message_id},
            {'buf': utils.hex_to_bytes("000000")},
            {'callback_status': utils.int_to_bytes_little(4, callback_status)},
            {'new_dme_world_id': utils.int_to_bytes_little(4, new_dme_world_id)}
        ]
        return packet

class CreateGameResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: CreateGameResponseHandler')


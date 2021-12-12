from enums.enums import MediusIdEnum
from enums.enums import MediusEnum
from utils import utils

class SetGameListFilterResponse0Serializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

    @classmethod
    def build(self, message_id, callback_status):
        packet = [
            {'name': __name__},
            {'mediusid': MediusIdEnum.SetGameListFilterResponse0},
            {'message_id': message_id},
            {'buf': utils.hex_to_bytes("000000")},
            {'callback_status': utils.int_to_bytes_little(4, callback_status)}
        ]
        return packet

class SetGameListFilterResponse0Handler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: SetGameListFilterResponse0Handler')


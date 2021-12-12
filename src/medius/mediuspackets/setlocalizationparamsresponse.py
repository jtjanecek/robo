from enums.enums import MediusIdEnum
from utils import utils

class SetLocalizationParamsResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

    @classmethod
    def build(self, message_id, callback_status):
        packet = [
            {'name': __name__},
            {'mediusid': MediusIdEnum.SetLocalizationParamsResponse},
            {'message_id': message_id},
            {'buf': utils.hex_to_bytes("000000")},
            {'callback_status': utils.int_to_bytes_little(4, callback_status)}
        ]
        return packet

class SetLocalizationParamsResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: SetLocalizationParamsResponseHandler')


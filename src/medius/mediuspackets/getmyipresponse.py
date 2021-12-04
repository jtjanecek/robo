from enums.enums import MediusIdEnum, MediusEnum
from utils import utils

class GetMyIPResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

    @classmethod
    def build(self,
            message_id,
            addr,
            callback_status
            ):
        return [
            {'name': __name__},
            {'mediusid': MediusIdEnum.GetMyIPResponse},
            {'message_id': message_id},
            {'ip': utils.str_to_bytes(addr, MediusEnum.IP_MAXLEN)},
            {'buf': utils.bytes_from_hex("000000")},
            {'callback_status': utils.int_to_bytes_little(4, callback_status)}
        ]

class GetMyIPResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: GetMyIPResponseHandler')


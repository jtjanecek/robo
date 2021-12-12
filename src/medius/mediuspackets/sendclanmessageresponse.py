from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from enums.enums import MediusIdEnum

class SendClanMessageResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
        {'name': 'session_key', 'n_bytes': MediusEnum.SESSIONKEY_MAXLEN, 'cast': None}
    ]

    @classmethod
    def build(self,
            message_id,
            callback_status
            ):
        packet = [
            {'name': __name__},
            {'mediusid': MediusIdEnum.SendClanMessageResponse},
            {'message_id': message_id},
            {'buf': utils.hex_to_bytes("000000")},
            {'callback_status': utils.int_to_bytes_little(4, callback_status, signed=True)}
        ]
        return packet

class SendClanMessageResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: SendClanMessageResponseHandler')


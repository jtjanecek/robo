from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from medius.mediuspackets.sessionendresponse import SessionEndResponseSerializer

class SessionEndSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
        {'name': 'session_key', 'n_bytes': MediusEnum.SESSIONKEY_MAXLEN, 'cast': None}
    ]

class SessionEndHandler:
    def process(self, serialized, monolith, con):
        return [SessionEndResponseSerializer.build(
            serialized['message_id'],
            CallbackStatus.SUCCESS
        )]


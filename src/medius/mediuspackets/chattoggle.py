from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from medius.mediuspackets.chattoggleresponse import ChatToggleResponseSerializer

class ChatToggleSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None}
    ]

class ChatToggleHandler:
    def process(self, serialized, monolith, con):
        return [ChatToggleResponseSerializer.build(
            serialized['message_id'],
            CallbackStatus.SUCCESS
        )]
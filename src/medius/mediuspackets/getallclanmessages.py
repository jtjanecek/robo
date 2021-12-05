from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from medius.mediuspackets.getallclanmessagesresponse import GetAllClanMessagesResponseSerializer


class GetAllClanMessagesSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
        {'name': 'session_key', 'n_bytes': MediusEnum.SESSIONKEY_MAXLEN, 'cast': None},
    ]

class GetAllClanMessagesHandler:
    def process(self, serialized, monolith, con):
        return [GetAllClanMessagesResponseSerializer.build(
            serialized['message_id'],
            CallbackStatus.NO_RESULT,
            0, # clan message id
            '', # message
            0, # clan message status
            1, # end of list
        )]


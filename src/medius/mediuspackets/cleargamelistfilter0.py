from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from medius.mediuspackets.cleargamelistfilterresponse import ClearGameListFilterResponseSerializer

class ClearGameListFilter0Serializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None}
    ]

class ClearGameListFilter0Handler:
    def process(self, serialized, monolith, con):
        return [ClearGameListFilterResponseSerializer.build(
            serialized['message_id'],
            CallbackStatus.SUCCESS
        )]
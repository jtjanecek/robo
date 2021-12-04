from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from medius.mediuspackets.getmyclansresponse import GetMyClansResponseSerializer

class GetMyClansSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
        {'name': 'session_key', 'n_bytes': MediusEnum.SESSIONKEY_MAXLEN, 'cast': None}
    ]

class GetMyClansHandler:
    def process(self, serialized, monolith, con):
        return [GetMyClansResponseSerializer.build(
            serialized['message_id'],
            CallbackStatus.NO_RESULT,
            0, # Clan id
            0, # app id
            "",
            0, # leader account id
            "", # Leader account name
            "", # stats
            0, # clan status
            1 # end of list
        )]

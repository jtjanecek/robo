from enums.enums import MediusEnum, CallbackStatus, MediusPlayerStatus
from utils import utils
from medius.mediuspackets.getignorelistresponse import GetIgnoreListResponseSerializer

class GetIgnoreListSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None}
    ]

class GetIgnoreListHandler:
    def process(self, serialized, monolith, con):
        return [GetIgnoreListResponseSerializer.build(
            serialized['message_id'],
            CallbackStatus.NO_RESULT,
            0, # ignore account id
            "", # account name
            MediusPlayerStatus.MEDIUS_PLAYER_DISCONNECTED, 
            1 # end of list
        )]

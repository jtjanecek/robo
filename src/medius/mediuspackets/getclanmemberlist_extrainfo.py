from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from medius.mediuspackets.getclanmemberlist_extrainforesponse import GetClanMemberList_ExtraInfoResponseSerializer

class GetClanMemberList_ExtraInfoSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
    ]

class GetClanMemberList_ExtraInfoHandler:
    def process(self, serialized, monolith, con):
        return [GetClanMemberList_ExtraInfoResponseSerializer.build(
            serialized['message_id'],
            CallbackStatus.NO_RESULT,
            0, # account id
            "", # account name
            "", # account stats
            0, # mediusPlayerOnlineStats
            0,  # ladderstat
            0,  # ladderposition
            0,  # totalrankings
            1 # end of list
        )]

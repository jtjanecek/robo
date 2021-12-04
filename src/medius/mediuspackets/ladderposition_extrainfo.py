from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from medius.mediuspackets.ladderposition_extrainforesponse import LadderPosition_ExtraInfoResponseSerializer

class LadderPosition_ExtraInfoSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None}
    ]

class LadderPosition_ExtraInfoHandler:
    def process(self, serialized, monolith, con):
        return [LadderPosition_ExtraInfoResponseSerializer.build(
                serialized['message_id'],
                CallbackStatus.SUCCESS,
                1, # ladder position,
                1, # ladder stat,
                1, # account_id
                "", # username
                "", # account stats
                0, # onlinestate1,
                0, # onlinestate2,
                0, # onlinestate3,
                "", # onlinestatelobbyname
                "", # onlinestategamename
                1 # endoflist
            )]
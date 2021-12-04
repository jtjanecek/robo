from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from medius.mediuspackets.addtobuddylistresponse import AddToBuddyListResponseSerializer

class AddToBuddyListSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None}
    ]

class AddToBuddyListHandler:
    def process(self, serialized, monolith, con):
        return [AddToBuddyListResponseSerializer.build(
                serialized['message_id'],
                CallbackStatus.SUCCESS
            )]

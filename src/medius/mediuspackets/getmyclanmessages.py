from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from medius.mediuspackets.getmyclanmessagesresponse import GetMyClanMessagesResponseSerializer


class GetMyClanMessagesSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
        {'name': 'session_key', 'n_bytes': MediusEnum.SESSIONKEY_MAXLEN, 'cast': None},
        {'name': 'buf', 'n_bytes': 2, 'cast': None},
        {'name': 'clan_id', 'n_bytes': 4, 'cast': utils.bytes_to_int_little}
    ]


class GetMyClanMessagesHandler:
    def process(self, serialized, monolith, con):
        return [GetMyClanMessagesResponseSerializer.build(
            serialized['message_id'],
            CallbackStatus.SUCCESS,
            serialized['clan_id'],
            'Test Clan Message',
            1
        )]


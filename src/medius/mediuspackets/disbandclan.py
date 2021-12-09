from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from medius.mediuspackets.disbandclanresponse import DisbandClanResponseSerializer

class DisbandClanSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
        {'name': 'session_key', 'n_bytes': MediusEnum.SESSIONKEY_MAXLEN, 'cast': None},
        {'name': 'buf', 'n_bytes': 2, 'cast': None},
        {'name': 'clan_id', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
    ]

class DisbandClanHandler:
    def process(self, serialized, monolith, con):

        client_manager = monolith.get_client_manager()
        client_manager.disband_clan(serialized['clan_id'])

        return [DisbandClanResponseSerializer.build(
            serialized['message_id'],
            CallbackStatus.SUCCESS
        )]
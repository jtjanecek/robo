from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from medius.mediuspackets.removeplayerfromclanresponse import RemovePlayerFromClanResponseSerializer

class RemovePlayerFromClanSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
        {'name': 'session_key', 'n_bytes': MediusEnum.SESSIONKEY_MAXLEN, 'cast': None},
        {'name': 'buf', 'n_bytes': 2, 'cast': None},
        {'name': 'account_id', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
        {'name': 'clan_id', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
    ]

class RemovePlayerFromClanHandler:
    def process(self, serialized, monolith, con):
        client_manager = monolith.get_client_manager()
        client_manager.remove_player_from_clan(serialized['account_id'], serialized['clan_id'])

        return [RemovePlayerFromClanResponseSerializer.build(
            serialized['message_id'],
            CallbackStatus.SUCCESS
        )]

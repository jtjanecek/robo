from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from medius.mediuspackets.accountupdatestatsresponse import AccountUpdateStatsResponseSerializer

class AccountUpdateStatsSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
        {'name': 'session_key', 'n_bytes': MediusEnum.SESSIONKEY_MAXLEN, 'cast': None},
        {'name': 'stats', 'n_bytes': MediusEnum.ACCOUNTSTATS_MAXLEN, 'cast': utils.bytes_to_hex}
    ]

class AccountUpdateStatsHandler:
    def process(self, serialized, monolith, con):
        client_manager = monolith.get_client_manager()

        account_id = client_manager.get_account_id(session_key = serialized['session_key'])

        client_manager.update_player_stats(account_id, serialized['stats'])

        return [AccountUpdateStatsResponseSerializer.build(
            serialized['message_id'],
            CallbackStatus.SUCCESS
        )]
from medius.mediuspackets.getclanbyidresponse import GetClanByIDResponseSerializer
from utils import utils
from enums.enums import CallbackStatus, MediusEnum

class GetClanByIDSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
        {'name': 'session_key', 'n_bytes': MediusEnum.SESSIONKEY_MAXLEN, 'cast': None},
        {'name': 'buf', 'n_bytes': 2, 'cast': None},
        {'name': 'account_id', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
        {'name': 'clan_id', 'n_bytes': 4, 'cast': utils.bytes_to_int_little}
    ]

class GetClanByIDHandler:
    def process(self, serialized, monolith, con):
        clan_id = serialized['clan_id']
        app_id = monolith.get_app_id()
        clan_status = 0

        client_manager = monolith.get_client_manager()
        clan_name = client_manager.get_clan_name(clan_id)
        leader_account_id = client_manager.get_clan_leader_account_id(clan_id)

        clan_info = client_manager.get_clan_info(clan_id)
        leader_account_name = clan_info['leader_account_name']
        stats = clan_info['clan_stats']

        return [GetClanByIDResponseSerializer.build(
            serialized['message_id'],
            CallbackStatus.SUCCESS,
            app_id,
            clan_name,
            leader_account_id,
            leader_account_name,
            stats,
            clan_status
        )]
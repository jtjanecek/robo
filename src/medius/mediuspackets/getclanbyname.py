from utils import utils
from enums.enums import CallbackStatus, MediusEnum
from medius.mediuspackets.getclanbynameresponse import GetClanByNameResponseSerializer


class GetClanByNameSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
        {'name': 'session_key', 'n_bytes': MediusEnum.SESSIONKEY_MAXLEN, 'cast': None},
        {'name': 'buf', 'n_bytes': 2, 'cast': None},
        {'name': 'app_id', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
        {'name': 'clan_name', 'n_bytes': MediusEnum.CLANNAME_MAXLEN, 'cast': utils.bytes_to_str}
    ]

class GetClanByNameHandler:
    def process(self, serialized, monolith, con):
        client_manager = monolith.get_client_manager()

        clan_id = client_manager.get_clan_id_from_name(serialized['clan_name'])

        if clan_id == None:
            # No response
            callback_status = CallbackStatus.NO_RESULT
            clan_id = 0
            leader_account_id = 0
            leader_account_name = ''
            stats = '00' * MediusEnum.CLANSTATS_MAXLEN
            clan_status = 0
        else:
            callback_status = CallbackStatus.SUCCESS
            leader_account_id = client_manager.get_clan_leader_account_id(clan_id)
            clan_info = client_manager.get_clan_info(clan_id)
            leader_account_name = clan_info['leader_account_name']
            stats = clan_info['clan_stats']
            clan_status = 0

        return [GetClanByNameResponseSerializer.build(
            serialized['message_id'],
            callback_status,
            clan_id,
            leader_account_id,
            leader_account_name,
            stats,
            clan_status
        )]
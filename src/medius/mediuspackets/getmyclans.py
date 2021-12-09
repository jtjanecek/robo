from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from medius.mediuspackets.getmyclansresponse import GetMyClansResponseSerializer

class GetMyClansSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
        {'name': 'session_key', 'n_bytes': MediusEnum.SESSIONKEY_MAXLEN, 'cast': None}
    ]

class GetMyClansHandler:
    def process(self, serialized, monolith, con):
        player = monolith.get_client_manager().get_player_from_mls_con(con)

        account_id = player.get_account_id()

        # Get the clan id associated with this user
        clan_id = monolith.get_client_manager().get_clan_id_from_account_id(account_id)

        if clan_id == None:
            callback_status = CallbackStatus.NO_RESULT
            clan_info = {
                'clan_id': 0,
                'clan_name': '',
                'leader_account_id': 0,
                'leader_account_name': '',
                'clan_stats': '',
                'clan_status': 0
            }
        else:
            clan_info = monolith.get_client_manager().get_clan_info(clan_id)
            callback_status = CallbackStatus.SUCCESS

        return [GetMyClansResponseSerializer.build(
            serialized['message_id'],
            callback_status,
            clan_info['clan_id'], # Clan id
            10684, # app id
            clan_info['clan_name'],
            clan_info['leader_account_id'], # leader account id
            clan_info['leader_account_name'], # Leader account name
            clan_info['clan_stats'], # stats
            clan_info['clan_status'], # clan status
            1 # end of list
        )]

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
        client_manager = monolith.get_client_manager()
        player = client_manager.get_player_from_mls_con(con)
        account_id = player.get_account_id()

        clan_id = client_manager.get_clan_id_from_account_id(account_id)
        clan_message = client_manager.get_clan_message(serialized['clan_id'])

        return [GetMyClanMessagesResponseSerializer.build(
            serialized['message_id'],
            CallbackStatus.SUCCESS,
            serialized['clan_id'],
            clan_message,
            1
        )]


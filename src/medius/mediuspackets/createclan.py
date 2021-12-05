from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from medius.mediuspackets.createclanresponse import CreateClanResponseSerializer

class CreateClanSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
        {'name': 'session_key', 'n_bytes': MediusEnum.SESSIONKEY_MAXLEN, 'cast': None},
        {'name': 'buf', 'n_bytes': 2, 'cast': None},
        {'name': 'app_id', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
        {'name': 'clan_name', 'n_bytes': MediusEnum.CLANNAME_MAXLEN, 'cast': None},
    ]

class CreateClanHandler:
    def process(self, serialized, monolith, con):

        player = monolith.get_client_manager().get_player_from_mls_con(con)
        player_username = player.get_username()
        player_account_id = player.get_account_id()

        new_clan_id = monolith.get_client_manager().create_clan(serialized['clan_name'], player_account_id, player_username)

        if new_clan_id == None:
            callback_status = CallbackStatus.CLAN_NAME_IN_USE
            new_clan_id = 0
        else:
            callback_status = CallbackStatus.SUCCESS

        return [CreateClanResponseSerializer.build(
            serialized['message_id'],
            callback_status,
            new_clan_id
        )]
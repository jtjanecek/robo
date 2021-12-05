from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from medius.mediuspackets.sendclanmessageresponse import SendClanMessageResponseSerializer

class SendClanMessageSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
        {'name': 'session_key', 'n_bytes': MediusEnum.SESSIONKEY_MAXLEN, 'cast': None},
        {'name': 'clan_message', 'n_bytes': MediusEnum.CLANMSG_MAXLEN, 'cast': None}
    ]

class SendClanMessageHandler:
    def process(self, serialized, monolith, con):

        client_manager = monolith.get_client_manager()
        player = client_manager.get_player_from_mls_con(con)
        account_id = player.get_account_id()

        clan_id = client_manager.get_clan_id_from_account_id(account_id)
        clan_message = utils.bytes_to_str(serialized['clan_message'])

        client_manager.update_clan_message(clan_id, clan_message)

        return [SendClanMessageResponseSerializer.build(
            serialized['message_id'],
            CallbackStatus.SUCCESS
        )]

from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from medius.mediuspackets.getallclanmessagesresponse import GetAllClanMessagesResponseSerializer


class GetAllClanMessagesSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
        {'name': 'session_key', 'n_bytes': MediusEnum.SESSIONKEY_MAXLEN, 'cast': None},
    ]

class GetAllClanMessagesHandler:
    def process(self, serialized, monolith, con):

        client_manager = monolith.get_client_manager()
        player = client_manager.get_player_from_mls_con(con)
        account_id = player.get_account_id()

        clan_id = client_manager.get_clan_id_from_account_id(account_id)
        clan_message = client_manager.get_clan_message(clan_id)

        return [GetAllClanMessagesResponseSerializer.build(
            serialized['message_id'],
            CallbackStatus.SUCCESS,
            0, # clan message id
            clan_message, # message
            0, # clan message status
            1, # end of list
        )]


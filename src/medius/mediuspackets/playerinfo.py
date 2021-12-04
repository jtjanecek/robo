from utils import utils
from enums.enums import MediusEnum, CallbackStatus
from medius.mediuspackets.playerinforesponse import PlayerInfoResponseSerializer

class PlayerInfoSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
        {'name': 'session_key', 'n_bytes': MediusEnum.SESSIONKEY_MAXLEN, 'cast': None},
        {'name': 'buf', 'n_bytes': 2, 'cast': None},
        {'name': 'account_id', 'n_bytes': 4, 'cast': utils.bytes_to_int_little}
    ]

class PlayerInfoHandler:
    def process(self, serialized, monolith, con):

        account_id = serialized['account_id']

        client_manager = monolith.get_client_manager()
        account_name = client_manager.get_username(account_id=account_id)
        player_status = client_manager.get_player_status(account_id)
        connection_class = 1
        stats = client_manager.get_player_stats(account_id)
        return [PlayerInfoResponseSerializer.build(
            serialized['message_id'],
            CallbackStatus.SUCCESS,
            account_name,
            monolith.get_app_id(),
            player_status,
            connection_class,
            stats
        )]
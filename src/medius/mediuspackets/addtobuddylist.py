from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from medius.mediuspackets.addtobuddylistresponse import AddToBuddyListResponseSerializer

class AddToBuddyListSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
        {'name': 'session_key', 'n_bytes': MediusEnum.SESSIONKEY_MAXLEN, 'cast': None},
        {'name': 'buf', 'n_bytes': 2, 'cast': None},
        {'name': 'account_id', 'n_bytes': 4, 'cast': utils.bytes_to_int_little}
    ]

class AddToBuddyListHandler:
    def process(self, serialized, monolith, con):

        player = monolith.get_client_manager().get_player_from_mls_con(con)
        player_account_id = player.get_account_id()

        monolith.get_client_manager().add_buddy(player_account_id, serialized['account_id'])

        return [AddToBuddyListResponseSerializer.build(
                serialized['message_id'],
                CallbackStatus.SUCCESS
            )]

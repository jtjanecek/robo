from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from medius.mediuspackets.transferclanleadershipresponse import TransferClanLeadershipResponseSerializer

class TransferClanLeadershipSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
        {'name': 'session_key', 'n_bytes': MediusEnum.SESSIONKEY_MAXLEN, 'cast': None},
        {'name': 'buf', 'n_bytes': 2, 'cast': None},
        {'name': 'new_account_id', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
        {'name': 'new_account_name', 'n_bytes': MediusEnum.ACCOUNTNAME_MAXLEN, 'cast': utils.bytes_to_str},
    ]

class TransferClanLeadershipHandler:
    def process(self, serialized, monolith, con):

        client_manager = monolith.get_client_manager()
        player = client_manager.get_player_from_mls_con(con)
        account_id = player.get_account_id()

        clan_id = client_manager.get_clan_id_from_account_id(account_id)

        client_manager.transfer_clan_ownership(clan_id, serialized['new_account_id'], serialized['new_account_name'])

        return [TransferClanLeadershipResponseSerializer.build(
            serialized['message_id'],
            CallbackStatus.SUCCESS
        )]


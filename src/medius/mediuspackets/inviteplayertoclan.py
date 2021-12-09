from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from medius.mediuspackets.inviteplayertoclanresponse import InvitePlayerToClanResponseSerializer

class InvitePlayerToClanSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
        {'name': 'session_key', 'n_bytes': MediusEnum.SESSIONKEY_MAXLEN, 'cast': None},
        {'name': 'buf', 'n_bytes': 2, 'cast': None},
        {'name': 'account_id', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
        {'name': 'invite_message', 'n_bytes': MediusEnum.CLANMSG_MAXLEN, 'cast': utils.bytes_to_str}
    ]

class InvitePlayerToClanHandler:
    def process(self, serialized, monolith, con):
        client_manager = monolith.get_client_manager()
        account_id = client_manager.get_player_from_mls_con(con).get_account_id()
        clan_id = client_manager.get_clan_id_from_account_id(account_id)

        client_manager.invite_player_to_clan(serialized['account_id'], clan_id, serialized['invite_message'])

        return [InvitePlayerToClanResponseSerializer.build(
            serialized['message_id'],
            CallbackStatus.SUCCESS
        )]

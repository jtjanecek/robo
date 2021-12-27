from enums.enums import CallbackStatus, MediusEnum
from utils import utils
from medius.mediuspackets.revokeclaninvitationresponse import RevokeClanInvitationResponseSerializer

class RevokeClanInvitationSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
        {'name': 'session_key', 'n_bytes': MediusEnum.SESSIONKEY_MAXLEN, 'cast': None},
        {'name': 'buf', 'n_bytes': 2, 'cast': None},
        {'name': 'player_account_id', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
    ]

class RevokeClanInvitationHandler:
    def process(self, serialized, monolith, con):

        client_manager = monolith.get_client_manager()
        account_id = client_manager.get_player_from_mls_con(con).get_account_id()
        clan_id = client_manager.get_clan_id_from_account_id(account_id)

        client_manager.remove_clan_invite(clan_id, serialized['player_account_id'])

        return [RevokeClanInvitationResponseSerializer.build(
            serialized['message_id'],
            CallbackStatus.SUCCESS
        )]
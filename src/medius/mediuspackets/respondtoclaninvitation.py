from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from medius.mediuspackets.respondtoclaninvitationresponse import RespondToClanInvitationResponseSerializer

class RespondToClanInvitationSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
        {'name': 'session_key', 'n_bytes': MediusEnum.SESSIONKEY_MAXLEN, 'cast': None},
        {'name': 'buf', 'n_bytes': 2, 'cast': None},
        {'name': 'clan_invitation_id', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
        {'name': 'response', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
    ]

class RespondToClanInvitationHandler:
    def process(self, serialized, monolith, con):

        client_manager = monolith.get_client_manager()

        if serialized['response'] == 0: # undecided
            pass
        elif serialized['response'] == 1: # accept
            client_manager.respond_clan_invite(serialized['clan_invitation_id'], True)
        elif serialized['response'] == 2: # reject
            client_manager.respond_clan_invite(serialized['clan_invitation_id'], False)
        elif serialized['response'] == 3: # decline
            client_manager.respond_clan_invite(serialized['clan_invitation_id'], False)

        return [RespondToClanInvitationResponseSerializer.build(
            serialized['message_id'],
            CallbackStatus.SUCCESS
        )]

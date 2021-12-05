from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from medius.mediuspackets.checkmyclaninvitationsresponse import CheckMyClanInvitationsResponseSerializer

class CheckMyClanInvitationsSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
    ]

class CheckMyClanInvitationsHandler:
    def process(self, serialized, monolith, con):
        return [CheckMyClanInvitationsResponseSerializer.build(
            serialized['message_id'],
            CallbackStatus.NO_RESULT
        )]

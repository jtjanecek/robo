from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from medius.mediuspackets.accountgetidresponse import AccountGetIdResponseSerializer

class AccountGetIdSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
        {'name': 'session_key', 'n_bytes': MediusEnum.SESSIONKEY_MAXLEN, 'cast': None}
    ]

class AccountGetIdHandler:
    def process(self, serialized, monolith, con):
        account_id = monolith.get_client_manager().get_account_id(session_key=serialized['session_key'])

        if account_id == None:
            return [AccountGetIdResponseSerializer.build(
                    serialized['message_id'],
                    0,
                    CallbackStatus.NO_RESULT
                )]
        else:
            return [AccountGetIdResponseSerializer.build(
                    serialized['message_id'],
                    account_id,
                    CallbackStatus.SUCCESS
                )]
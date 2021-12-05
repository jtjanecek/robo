from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from medius.mediuspackets.accountgetidresponse import AccountGetIdResponseSerializer

class AccountGetIdSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
        {'name': 'session_key', 'n_bytes': MediusEnum.SESSIONKEY_MAXLEN, 'cast': None},
        {'name': 'account_name', 'n_bytes': MediusEnum.ACCOUNTNAME_MAXLEN, 'cast': utils.bytes_to_str}
    ]

class AccountGetIdHandler:
    def process(self, serialized, monolith, con):
        account_id = monolith.get_client_manager().get_account_id(username=serialized['account_name'])

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

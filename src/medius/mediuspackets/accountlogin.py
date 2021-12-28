from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from medius.mediuspackets.accountloginresponse import AccountLoginResponseSerializer

class AccountLoginSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
        {'name': 'session_key', 'n_bytes': MediusEnum.SESSIONKEY_MAXLEN, 'cast': None},
        {'name': 'username', 'n_bytes': 14, 'cast': utils.bytes_to_str},
        {'name': 'buf', 'n_bytes': 18, 'cast': None},
        {'name': 'password', 'n_bytes': 14, 'cast': utils.sha512_encrypt}
    ]

class AccountLoginHandler:
    def process(self, serialized, monolith, con):
        client_manager = monolith.get_client_manager()
        if client_manager.account_login(serialized['username'], serialized['password'], serialized['session_key']):
            callback_status = CallbackStatus.SUCCESS
        else:
            callback_status = CallbackStatus.INVALID_PASSWORD

        account_id = client_manager.get_account_id(serialized['username'])

        access_key = client_manager.generate_access_key()
        account_type = client_manager.get_account_type(account_id)

        world_id = 0

        mls_ip = monolith.get_mls_ip()
        mls_port = monolith.get_mls_port()
        nat_ip = monolith.get_nat_ip()
        nat_port = monolith.get_nat_port()

        return [AccountLoginResponseSerializer.build(
            serialized['message_id'],
            callback_status,
            account_id,
            account_type,
            world_id,
            mls_ip,
            mls_port,
            nat_ip,
            nat_port,
            serialized['session_key'],
            access_key
        )]

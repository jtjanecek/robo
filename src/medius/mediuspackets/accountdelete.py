from enums.enums import MediusEnum, CallbackStatus
from utils import utils

class AccountDeleteSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
        {'name': 'session_key', 'n_bytes': MediusEnum.SESSIONKEY_MAXLEN, 'cast': None},
        {'name': 'password', 'n_bytes': 14, 'cast': utils.Encrypter.sha512_encrypt_bcrypt}
    ]

class AccountDeleteHandler:
    def process(self, serialized, monolith, con):
        client_manager = monolith.get_client_manager()
        client_manager.delete_user(serialized['session_key'], serialized['password'])
        return []

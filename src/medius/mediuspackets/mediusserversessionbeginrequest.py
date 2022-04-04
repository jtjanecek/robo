from enums.enums import MediusEnum, CallbackStatus
from utils import utils

from medius.mediuspackets.mediusserversessionbeginresponse import MediusServerSessionBeginResponseSerializer

class MediusServerSessionBeginRequestSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
        {'name': 'buf', 'n_bytes': 3, 'cast': None},
        {'name': 'connection_type', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
        {'name': 'app_id', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
        {'name': 'unk2', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
        {'name': 'version', 'n_bytes': None, 'cast': utils.bytes_to_str}
    ]

class MediusServerSessionBeginRequestHandler:
    def process(self, serialized, monolith, con):

        if con.server_name != 'mas':
            raise Exception(f'Cannot begin session from any server except mas: {con}, {serialized}')

        client_manager = monolith.get_client_manager()
        session_key = client_manager.generate_session_key()

        return [MediusServerSessionBeginResponseSerializer.build(serialized['message_id'], CallbackStatus.SUCCESS, session_key)]

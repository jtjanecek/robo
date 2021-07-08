from enums.enums import MediusEnum, CallbackStatus
from utils import utils

from medius.mediuspackets.sessionbeginresponse import SessionBeginResponseSerializer

class SessionBeginSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None},
		{'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
		{'name': 'buf', 'n_bytes': 3, 'cast': None},
		{'name': 'connection_type', 'n_bytes': 4, 'cast': utils.bytes_to_int_little}
	]
	
class SessionBeginHandler:
	def process(self, serialized, monolith, con):

		if con.server_name != 'mas':
			raise Exception(f'Cannot begin session from any server except mas: {con}, {serialized}')

		client_manager = monolith.get_client_manager()
		session_key = client_manager.generate_session_key()

		return [SessionBeginResponseSerializer.build(serialized['message_id'], CallbackStatus.SUCCESS, session_key)]


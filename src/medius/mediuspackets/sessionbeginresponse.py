from enums.enums import MediusIdEnum
from utils import utils

class SessionBeginResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None},
	]

	@classmethod
	def build(self, message_id: bytes, callback_status: int, session_key: bytes):
		packet = [
			{'name': __name__},
			{'mediusid': MediusIdEnum.SessionBeginResponse},
			{'message_id': message_id},
			{'buf': utils.bytes_from_hex("000000")},
			{'callback_status': utils.int_to_bytes_little(4, callback_status)},
			{'session_key': session_key},
			{'buf': utils.bytes_from_hex("000000")}
		]
		return packet

class SessionBeginResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: SessionBeginResponseHandler')


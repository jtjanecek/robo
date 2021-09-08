from enums.enums import MediusIdEnum
from enums.enums import MediusEnum
from utils import utils

class TextFilterResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

	@classmethod
	def build(self,
			message_id,
			text,
			callback_status
		):
		packet = [
			{'name': __name__},
			{'mediusid': MediusIdEnum.TextFilterResponse},
			{'message_id': message_id},
			{'text': text},
			{'buf': utils.bytes_from_hex("000000")},
			{'callback_status': utils.int_to_bytes_little(4, callback_status)}
		]
		return packet

class TextFilterResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: TextFilterResponseHandler')


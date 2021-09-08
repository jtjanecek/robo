from enums.enums import MediusIdEnum, MediusEnum
from utils import utils

class ChatFwdMessageSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

	@classmethod
	def build(self,			
			message_id: bytes,
			source_account_id: int,
			username: int,
			message_type: int,
			text: bytes
			):
		packet = [
			{'name': __name__},
			{'mediusid': MediusIdEnum.ChatFwdMessage},
			{'message_id': message_id},
			{'buf': utils.bytes_from_hex("000000")},
			{'source_account_id': utils.int_to_bytes_little(4, source_account_id)},
			{'username': utils.str_to_bytes(username, MediusEnum.USERNAME_MAXLEN)},
			{'message_type': utils.int_to_bytes_little(4, message_type)},
			{'text': text}
		]
		return packet

class ChatFwdMessageHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: ChatFwdMessageHandler')


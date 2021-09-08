from enums.enums import MediusIdEnum
from enums.enums import MediusEnum
from utils import utils

class GameWorldPlayerListResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

	@classmethod
	def build(self,
			message_id: bytes,
			callback_status: int,
			account_id: int,
			username: str,
			stats: bytes,
			connection_class: int,
			end_of_list: int):
		packet = [
			{'name': __name__},
			{'mediusid': MediusIdEnum.GameWorldPlayerListResponse},
			{'message_id': message_id},
			{'buf': utils.bytes_from_hex("000000")},
			{'callback_status': utils.int_to_bytes_little(4, callback_status)},
			{'account_id': utils.int_to_bytes_little(4, account_id)},
			{'username': utils.str_to_bytes(username, MediusEnum.ACCOUNTNAME_MAXLEN)},
			{'stats': stats},
			{'connection_class': utils.int_to_bytes_little(4, connection_class)},
			{'end_of_list': utils.int_to_bytes_little(4, end_of_list)}
		]
		return packet

class GameWorldPlayerListResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: GameWorldPlayerListResponseHandler')


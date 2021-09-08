from enums.enums import MediusEnum
from utils import utils

class UpdateUserStateSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None},
		{'name': 'session_key', 'n_bytes': MediusEnum.SESSIONKEY_MAXLEN, 'cast': None},
		{'name': 'buf', 'n_bytes': 3, 'cast': None},
		{'name': 'user_action', 'n_bytes': 4, 'cast': utils.bytes_to_int_little}
	]

class UpdateUserStateHandler:
	def process(self, serialized, monolith, con):
		return []


from utils import utils
from enums.enums import RtIdEnum

class ServerCryptkeyGameSerializer:
	data_dict = [
		{'name': 'rtid', 'n_bytes': 1, 'cast': None},
		{'name': 'len', 'n_bytes': 2, 'cast': utils.bytes_to_int_little},
	]

	def serialize(self, data: bytes):
		raise Exception('Unimplemented Handler: ServerCryptkeyGameSerializer')
		return utils.serialize(data, self.data_dict)

	@classmethod
	def build(self, key):
		packet = [
			{'name': __name__},
			{'rtid': RtIdEnum.SERVER_CRYPTKEY_GAME},
			{'key': key}
		]
		return packet

class ServerCryptkeyGameHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: ServerCryptkeyGameHandler')


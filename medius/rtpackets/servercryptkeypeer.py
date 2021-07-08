from enums.enums import RtIdEnum
from utils import utils

class ServerCryptkeyPeerSerializer:
	data_dict = [
		{'name': 'rtid', 'n_bytes': 1, 'cast': None},
		{'name': 'len', 'n_bytes': 2, 'cast': utils.bytes_to_int_little},
		{'name': 'key', 'n_bytes': 64, 'cast': utils.bytes_to_int_little}
	]

	def serialize(self, data: bytes):
		raise Exception('Unimplemented Handler: ServerCryptkeyPeerSerializer')
		return utils.serialize(data, self.data_dict)

	@classmethod
	def build(self, data: bytes):
		packet = [
			{'name': __name__},
			{'rtid': RtIdEnum.SERVER_CRYPTKEY_PEER},
			{'key': data}
		]
		return packet

class ServerCryptkeyPeerHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: ServerCryptkeyPeerHandler')


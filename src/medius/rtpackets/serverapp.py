from enums.enums import RtIdEnum
from utils import utils

class ServerAppSerializer:
	data_dict = [
		{'name': 'rtid', 'n_bytes': 1, 'cast': None},
		{'name': 'len', 'n_bytes': 2, 'cast': utils.bytes_to_int_little}
	]

	def serialize(self, data: bytes):
		raise Exception('Unimplemented Handler: ServerAppSerializer')
		return utils.serialize(data, self.data_dict)

	@classmethod
	def build(self, payload):
		packet = [
			{'name': __name__},
			{'rtid': RtIdEnum.SERVER_APP},
			{'payload': payload}
		]
		return packet

class ServerAppHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: ServerAppHandler')


from enums.enums import RtIdEnum
from utils import utils

class ClientEchoSerializer:
	data_dict = [
		{'name': 'rtid', 'n_bytes': 1, 'cast': None},
		{'name': 'len', 'n_bytes': 1, 'cast': utils.bytes_to_int_little},
		{'name': 'heartbeat', 'n_bytes': 1, 'cast': None}
	]

	def serialize(self, data: bytes):
		return utils.serialize(data, self.data_dict, __name__)

	@classmethod
	def build(self, heartbeat):
		packet = [
			{'name': __name__},
			{'rtid': RtIdEnum.CLIENT_ECHO},
			{'heartbeat': heartbeat}
		]
		return packet

class ClientEchoHandler:
	def process(self, serialized, monolith, con):
		return [ClientEchoSerializer.build(serialized['heartbeat'])]

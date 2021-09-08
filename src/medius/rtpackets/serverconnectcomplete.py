
from utils import utils
from enums.enums import RtIdEnum

class ServerConnectCompleteSerializer:
	data_dict = [
		{'name': 'rtid', 'n_bytes': 1, 'cast': None},
		{'name': 'len', 'n_bytes': 2, 'cast': utils.bytes_to_int_little}
	]

	def serialize(self, data: bytes):
		raise Exception('Unimplemented Handler: ServerConnectCompleteSerializer')
		return utils.serialize(data, self.data_dict)

	@classmethod
	def build(self, player_count=1):
		packet = [
			{'name': __name__},
			{'rtid': RtIdEnum.SERVER_CONNECT_COMPLETE},
			{'connect_complete': utils.int_to_bytes_little(2, player_count)}
		]
		return packet

class ServerConnectCompleteHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: ServerConnectCompleteHandler')


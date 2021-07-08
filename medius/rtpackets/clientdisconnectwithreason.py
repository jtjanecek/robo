
from utils import utils

class ClientDisconnectWithReasonSerializer:
	data_dict = [
		{'name': 'rtid', 'n_bytes': 1, 'cast': None},
		{'name': 'len', 'n_bytes': 2, 'cast': utils.bytes_to_int_little}
	]

	def serialize(self, data: bytes):
		raise Exception('Unimplemented Handler: ClientDisconnectWithReasonSerializer')
		return utils.serialize(data, self.data_dict)

class ClientDisconnectWithReasonHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: ClientDisconnectWithReasonHandler')


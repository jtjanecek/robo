
from utils import utils

class GetAllClanMessagesResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class GetAllClanMessagesResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: GetAllClanMessagesResponseHandler')


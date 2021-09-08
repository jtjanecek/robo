
from utils import utils

class GenericChatSetFilterResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class GenericChatSetFilterResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: GenericChatSetFilterResponseHandler')


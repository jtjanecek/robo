
from utils import utils

class GenericChatMessageSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class GenericChatMessageHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: GenericChatMessageHandler')


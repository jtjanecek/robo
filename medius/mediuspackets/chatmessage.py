
from utils import utils

class ChatMessageSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class ChatMessageHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: ChatMessageHandler')


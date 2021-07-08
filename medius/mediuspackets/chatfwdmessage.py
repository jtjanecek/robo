
from utils import utils

class ChatFwdMessageSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class ChatFwdMessageHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: ChatFwdMessageHandler')


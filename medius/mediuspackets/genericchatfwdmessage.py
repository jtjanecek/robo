
from utils import utils

class GenericChatFwdMessageSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class GenericChatFwdMessageHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: GenericChatFwdMessageHandler')


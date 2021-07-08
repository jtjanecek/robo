
from utils import utils

class DMELANTextMessageSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class DMELANTextMessageHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: DMELANTextMessageHandler')



from utils import utils

class ModifyClanMessageSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class ModifyClanMessageHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: ModifyClanMessageHandler')


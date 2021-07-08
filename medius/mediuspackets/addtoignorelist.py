
from utils import utils

class AddToIgnoreListSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class AddToIgnoreListHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: AddToIgnoreListHandler')


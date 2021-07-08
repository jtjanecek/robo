
from utils import utils

class RemoveFromIgnoreListSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class RemoveFromIgnoreListHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: RemoveFromIgnoreListHandler')


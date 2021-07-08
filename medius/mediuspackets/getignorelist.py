
from utils import utils

class GetIgnoreListSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class GetIgnoreListHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: GetIgnoreListHandler')


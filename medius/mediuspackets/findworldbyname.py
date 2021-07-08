
from utils import utils

class FindWorldByNameSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class FindWorldByNameHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: FindWorldByNameHandler')


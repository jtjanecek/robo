
from utils import utils

class GetClanByNameSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class GetClanByNameHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: GetClanByNameHandler')


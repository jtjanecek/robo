
from utils import utils

class GetClanByIDSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class GetClanByIDHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: GetClanByIDHandler')



from utils import utils

class DisbandClanSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class DisbandClanHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: DisbandClanHandler')


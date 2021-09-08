
from utils import utils

class DisbandClanResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class DisbandClanResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: DisbandClanResponseHandler')


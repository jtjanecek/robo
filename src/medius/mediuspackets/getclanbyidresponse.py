
from utils import utils

class GetClanByIDResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class GetClanByIDResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: GetClanByIDResponseHandler')



from utils import utils

class GetClanByNameResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class GetClanByNameResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: GetClanByNameResponseHandler')



from utils import utils

class FindPlayerResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class FindPlayerResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: FindPlayerResponseHandler')


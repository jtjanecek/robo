
from utils import utils

class GetIgnoreListResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class GetIgnoreListResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: GetIgnoreListResponseHandler')


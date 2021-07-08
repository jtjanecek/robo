
from utils import utils

class GetTotalGamesResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class GetTotalGamesResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: GetTotalGamesResponseHandler')



from utils import utils

class UtilUpdateGameWorldResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class UtilUpdateGameWorldResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: UtilUpdateGameWorldResponseHandler')


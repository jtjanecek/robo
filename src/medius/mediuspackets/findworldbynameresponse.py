
from utils import utils

class FindWorldByNameResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class FindWorldByNameResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: FindWorldByNameResponseHandler')


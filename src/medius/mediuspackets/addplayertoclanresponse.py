
from utils import utils

class AddPlayerToClanResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class AddPlayerToClanResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: AddPlayerToClanResponseHandler')


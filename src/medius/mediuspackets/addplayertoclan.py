
from utils import utils

class AddPlayerToClanSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class AddPlayerToClanHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: AddPlayerToClanHandler')


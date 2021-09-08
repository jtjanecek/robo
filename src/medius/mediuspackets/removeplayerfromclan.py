
from utils import utils

class RemovePlayerFromClanSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class RemovePlayerFromClanHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: RemovePlayerFromClanHandler')


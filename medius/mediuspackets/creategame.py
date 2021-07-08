
from utils import utils

class CreateGameSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class CreateGameHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: CreateGameHandler')


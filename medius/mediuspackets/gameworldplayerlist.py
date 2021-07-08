
from utils import utils

class GameWorldPlayerListSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class GameWorldPlayerListHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: GameWorldPlayerListHandler')


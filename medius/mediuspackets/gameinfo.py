
from utils import utils

class GameInfoSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class GameInfoHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: GameInfoHandler')


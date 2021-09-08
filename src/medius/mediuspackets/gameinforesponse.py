
from utils import utils

class GameInfoResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class GameInfoResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: GameInfoResponseHandler')


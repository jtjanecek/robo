
from utils import utils

class LobbyWorldPlayerListResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class LobbyWorldPlayerListResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: LobbyWorldPlayerListResponseHandler')


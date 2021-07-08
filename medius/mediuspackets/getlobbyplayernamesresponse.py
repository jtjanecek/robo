
from utils import utils

class GetLobbyPlayerNamesResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class GetLobbyPlayerNamesResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: GetLobbyPlayerNamesResponseHandler')


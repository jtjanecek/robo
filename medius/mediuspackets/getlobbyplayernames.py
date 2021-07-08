
from utils import utils

class GetLobbyPlayerNamesSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class GetLobbyPlayerNamesHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: GetLobbyPlayerNamesHandler')


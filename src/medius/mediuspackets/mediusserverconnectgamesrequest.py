
from utils import utils

class MediusServerConnectGamesRequestSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class MediusServerConnectGamesRequestHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: MediusServerConnectGamesRequestHandler')


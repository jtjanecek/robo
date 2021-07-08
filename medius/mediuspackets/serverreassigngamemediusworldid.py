
from utils import utils

class ServerReassignGameMediusWorldIDSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class ServerReassignGameMediusWorldIDHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: ServerReassignGameMediusWorldIDHandler')


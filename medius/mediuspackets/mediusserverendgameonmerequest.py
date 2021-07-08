
from utils import utils

class MediusServerEndGameOnMeRequestSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class MediusServerEndGameOnMeRequestHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: MediusServerEndGameOnMeRequestHandler')


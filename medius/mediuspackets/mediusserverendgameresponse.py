
from utils import utils

class MediusServerEndGameResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class MediusServerEndGameResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: MediusServerEndGameResponseHandler')



from utils import utils

class MediusServerEndGameOnMeResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class MediusServerEndGameOnMeResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: MediusServerEndGameOnMeResponseHandler')


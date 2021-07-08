
from utils import utils

class MediusServerMoveGameWorldOnMeResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class MediusServerMoveGameWorldOnMeResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: MediusServerMoveGameWorldOnMeResponseHandler')


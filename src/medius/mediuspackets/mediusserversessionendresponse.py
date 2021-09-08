
from utils import utils

class MediusServerSessionEndResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class MediusServerSessionEndResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: MediusServerSessionEndResponseHandler')


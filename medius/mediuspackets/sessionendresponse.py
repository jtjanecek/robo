
from utils import utils

class SessionEndResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class SessionEndResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: SessionEndResponseHandler')


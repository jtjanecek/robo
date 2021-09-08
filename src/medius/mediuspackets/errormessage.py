
from utils import utils

class ErrorMessageSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class ErrorMessageHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: ErrorMessageHandler')


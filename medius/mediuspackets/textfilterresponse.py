
from utils import utils

class TextFilterResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class TextFilterResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: TextFilterResponseHandler')


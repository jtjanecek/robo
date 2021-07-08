
from utils import utils

class FileCreateResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class FileCreateResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: FileCreateResponseHandler')


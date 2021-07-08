
from utils import utils

class FileCloseResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class FileCloseResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: FileCloseResponseHandler')


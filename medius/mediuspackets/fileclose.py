
from utils import utils

class FileCloseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class FileCloseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: FileCloseHandler')


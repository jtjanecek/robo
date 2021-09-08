
from utils import utils

class FileCreateSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class FileCreateHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: FileCreateHandler')



from utils import utils

class FileUpdateAttributesSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class FileUpdateAttributesHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: FileUpdateAttributesHandler')



from utils import utils

class FileUpdateAttributesResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class FileUpdateAttributesResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: FileUpdateAttributesResponseHandler')



from utils import utils

class FileSearchByMetaDataSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class FileSearchByMetaDataHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: FileSearchByMetaDataHandler')


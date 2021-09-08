
from utils import utils

class FileUploadSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class FileUploadHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: FileUploadHandler')


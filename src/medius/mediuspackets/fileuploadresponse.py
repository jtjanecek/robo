
from utils import utils

class FileUploadResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class FileUploadResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: FileUploadResponseHandler')


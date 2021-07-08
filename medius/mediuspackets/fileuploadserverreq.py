
from utils import utils

class FileUploadServerReqSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class FileUploadServerReqHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: FileUploadServerReqHandler')


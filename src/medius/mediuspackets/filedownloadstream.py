
from utils import utils

class FileDownloadStreamSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class FileDownloadStreamHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: FileDownloadStreamHandler')



from utils import utils

class FileCancelOperationResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class FileCancelOperationResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: FileCancelOperationResponseHandler')


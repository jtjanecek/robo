
from utils import utils

class FileCancelOperationSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class FileCancelOperationHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: FileCancelOperationHandler')


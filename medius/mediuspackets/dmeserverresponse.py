
from utils import utils

class DMEServerResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class DMEServerResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: DMEServerResponseHandler')


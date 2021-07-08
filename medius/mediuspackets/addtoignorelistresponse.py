
from utils import utils

class AddToIgnoreListResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class AddToIgnoreListResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: AddToIgnoreListResponseHandler')


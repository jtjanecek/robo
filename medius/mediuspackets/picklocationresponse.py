
from utils import utils

class PickLocationResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class PickLocationResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: PickLocationResponseHandler')


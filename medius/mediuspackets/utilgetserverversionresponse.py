
from utils import utils

class UtilGetServerVersionResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class UtilGetServerVersionResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: UtilGetServerVersionResponseHandler')


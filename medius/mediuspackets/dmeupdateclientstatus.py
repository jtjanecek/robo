
from utils import utils

class DMEUpdateClientStatusSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class DMEUpdateClientStatusHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: DMEUpdateClientStatusHandler')


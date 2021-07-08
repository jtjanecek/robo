
from utils import utils

class FindPlayerSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class FindPlayerHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: FindPlayerHandler')



from utils import utils

class BanPlayerSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class BanPlayerHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: BanPlayerHandler')


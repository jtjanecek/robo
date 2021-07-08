
from utils import utils

class BinaryFwdMessageSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class BinaryFwdMessageHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: BinaryFwdMessageHandler')



from utils import utils

class SetMessageAsReadSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class SetMessageAsReadHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: SetMessageAsReadHandler')


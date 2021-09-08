
from utils import utils

class SetGameListFilterSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class SetGameListFilterHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: SetGameListFilterHandler')


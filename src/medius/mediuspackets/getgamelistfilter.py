
from utils import utils

class GetGameListFilterSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class GetGameListFilterHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: GetGameListFilterHandler')


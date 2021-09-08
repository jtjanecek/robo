
from utils import utils

class GetBuddyListSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class GetBuddyListHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: GetBuddyListHandler')


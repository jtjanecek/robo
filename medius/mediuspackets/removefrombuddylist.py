
from utils import utils

class RemoveFromBuddyListSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class RemoveFromBuddyListHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: RemoveFromBuddyListHandler')


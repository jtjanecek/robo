
from utils import utils

class AddToBuddyListSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class AddToBuddyListHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: AddToBuddyListHandler')


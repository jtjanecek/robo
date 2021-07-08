
from utils import utils

class AddToBuddyListResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class AddToBuddyListResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: AddToBuddyListResponseHandler')


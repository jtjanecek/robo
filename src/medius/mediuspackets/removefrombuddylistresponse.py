
from utils import utils

class RemoveFromBuddyListResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class RemoveFromBuddyListResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: RemoveFromBuddyListResponseHandler')


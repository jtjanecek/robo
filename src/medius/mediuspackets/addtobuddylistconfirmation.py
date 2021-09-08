
from utils import utils

class AddToBuddyListConfirmationSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class AddToBuddyListConfirmationHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: AddToBuddyListConfirmationHandler')


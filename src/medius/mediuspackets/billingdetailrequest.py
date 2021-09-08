
from utils import utils

class BillingDetailRequestSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class BillingDetailRequestHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: BillingDetailRequestHandler')


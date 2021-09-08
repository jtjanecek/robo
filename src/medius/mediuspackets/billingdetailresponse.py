
from utils import utils

class BillingDetailResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class BillingDetailResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: BillingDetailResponseHandler')


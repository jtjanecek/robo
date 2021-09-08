
from utils import utils

class BillingLoginResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class BillingLoginResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: BillingLoginResponseHandler')


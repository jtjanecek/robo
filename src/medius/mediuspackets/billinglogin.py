
from utils import utils

class BillingLoginSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class BillingLoginHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: BillingLoginHandler')


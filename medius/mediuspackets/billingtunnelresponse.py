
from utils import utils

class BillingTunnelResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class BillingTunnelResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: BillingTunnelResponseHandler')


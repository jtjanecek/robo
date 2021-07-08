
from utils import utils

class AccountGetProfileResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class AccountGetProfileResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: AccountGetProfileResponseHandler')



from utils import utils

class AccountDeleteResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class AccountDeleteResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: AccountDeleteResponseHandler')


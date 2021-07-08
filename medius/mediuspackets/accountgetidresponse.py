
from utils import utils

class AccountGetIdResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class AccountGetIdResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: AccountGetIdResponseHandler')


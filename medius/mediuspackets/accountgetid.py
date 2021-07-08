
from utils import utils

class AccountGetIdSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class AccountGetIdHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: AccountGetIdHandler')


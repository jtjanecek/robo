
from utils import utils

class AccountDeleteSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class AccountDeleteHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: AccountDeleteHandler')


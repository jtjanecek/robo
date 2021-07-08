
from utils import utils

class AccountGetProfileSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class AccountGetProfileHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: AccountGetProfileHandler')


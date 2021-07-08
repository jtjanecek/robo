
from utils import utils

class AccountUpdatePasswordSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class AccountUpdatePasswordHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: AccountUpdatePasswordHandler')


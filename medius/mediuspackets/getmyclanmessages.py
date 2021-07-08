
from utils import utils

class GetMyClanMessagesSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class GetMyClanMessagesHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: GetMyClanMessagesHandler')


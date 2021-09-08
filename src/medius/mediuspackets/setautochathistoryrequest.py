
from utils import utils

class SetAutoChatHistoryRequestSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class SetAutoChatHistoryRequestHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: SetAutoChatHistoryRequestHandler')


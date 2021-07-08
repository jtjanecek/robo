
from utils import utils

class SetAutoChatHistoryResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class SetAutoChatHistoryResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: SetAutoChatHistoryResponseHandler')


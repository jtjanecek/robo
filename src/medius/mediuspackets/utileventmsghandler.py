
from utils import utils

class UtilEventMsgHandlerSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class UtilEventMsgHandlerHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: UtilEventMsgHandlerHandler')


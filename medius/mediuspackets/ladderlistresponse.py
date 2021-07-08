
from utils import utils

class LadderListResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class LadderListResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: LadderListResponseHandler')


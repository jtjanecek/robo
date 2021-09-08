
from utils import utils

class LadderList_ExtraInfoResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class LadderList_ExtraInfoResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: LadderList_ExtraInfoResponseHandler')


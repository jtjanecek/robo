
from utils import utils

class LadderListSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class LadderListHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: LadderListHandler')


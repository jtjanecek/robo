
from utils import utils

class LadderPositionSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class LadderPositionHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: LadderPositionHandler')


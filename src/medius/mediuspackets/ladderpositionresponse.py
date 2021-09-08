
from utils import utils

class LadderPositionResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class LadderPositionResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: LadderPositionResponseHandler')


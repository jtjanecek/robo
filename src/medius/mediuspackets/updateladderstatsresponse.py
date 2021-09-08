
from utils import utils

class UpdateLadderStatsResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class UpdateLadderStatsResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: UpdateLadderStatsResponseHandler')


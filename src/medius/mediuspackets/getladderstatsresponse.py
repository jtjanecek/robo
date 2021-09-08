
from utils import utils

class GetLadderStatsResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class GetLadderStatsResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: GetLadderStatsResponseHandler')


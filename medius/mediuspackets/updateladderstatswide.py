
from utils import utils

class UpdateLadderStatsWideSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class UpdateLadderStatsWideHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: UpdateLadderStatsWideHandler')


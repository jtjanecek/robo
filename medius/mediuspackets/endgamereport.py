
from utils import utils

class EndGameReportSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class EndGameReportHandler:
	def process(self, serialized, monolith, con):
		# TODO: do some processing with this report
		return []


from utils import utils

class WorldReportSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class WorldReportHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: WorldReportHandler')



from utils import utils

class LadderPosition_ExtraInfoSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class LadderPosition_ExtraInfoHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: LadderPosition_ExtraInfoHandler')


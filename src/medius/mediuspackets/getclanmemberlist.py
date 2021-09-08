
from utils import utils

class GetClanMemberListSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class GetClanMemberListHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: GetClanMemberListHandler')


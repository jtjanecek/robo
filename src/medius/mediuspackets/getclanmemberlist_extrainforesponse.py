
from utils import utils

class GetClanMemberList_ExtraInfoResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class GetClanMemberList_ExtraInfoResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: GetClanMemberList_ExtraInfoResponseHandler')


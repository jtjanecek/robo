from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from medius.mediuspackets.getbuddylist_extrainforesponse import GetBuddyList_ExtraInfoResponseSerializer

class GetBuddyList_ExtraInfoSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None},
		{'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None}
	]

class GetBuddyList_ExtraInfoHandler:
	def process(self, serialized, monolith, con):
		return [GetBuddyList_ExtraInfoResponseSerializer.build(
			serialized['message_id'],
			"00000001000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001000000"
		)]

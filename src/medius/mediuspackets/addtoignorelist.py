from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from medius.mediuspackets.addtoignorelistresponse import AddToIgnoreListResponseSerializer

class AddToIgnoreListSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None},
		{'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None}
	]


class AddToIgnoreListHandler:
	def process(self, serialized, monolith, con):
		return [AddToIgnoreListResponseSerializer.build(
				serialized['message_id'],
				CallbackStatus.SUCCESS
			)]

from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from medius.mediuspackets.setgamelistfilterresponse0 import SetGameListFilterResponse0Serializer


class SetGameListFilter0Serializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None},
		{'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
		{'name': 'buf', 'n_bytes': 3, 'cast': None},
		{'name': 'filter_field', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
		{'name': 'mask', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
		{'name': 'comparison_operator', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
		{'name': 'baseline_value', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
	]

class SetGameListFilter0Handler:
	def process(self, serialized, monolith, con):
		return [SetGameListFilterResponse0Serializer.build(
			serialized['message_id'],
			CallbackStatus.SUCCESS
		)]
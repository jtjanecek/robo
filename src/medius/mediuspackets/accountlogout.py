from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from medius.mediuspackets.accountlogoutresponse import AccountLogoutResponseSerializer


class AccountLogoutSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None},
		{'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None}
	]

class AccountLogoutHandler:
	def process(self, serialized, monolith, con):
		return [AccountLogoutResponseSerializer.build(
			serialized['message_id'],
			CallbackStatus.SUCCESS
		)]

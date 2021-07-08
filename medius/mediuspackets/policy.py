from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from medius.mediuspackets.policyresponse import PolicyResponseSerializer

class PolicySerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None},
		{'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
		{'name': 'session_key', 'n_bytes': MediusEnum.SESSIONKEY_MAXLEN, 'cast': None}
	]

class PolicyHandler:
	def process(self, serialized, monolith, con):
		end_of_list = 1
		return [PolicyResponseSerializer.build(
			serialized['message_id'],
			CallbackStatus.SUCCESS,
			monolith.get_policy(),
			end_of_list
		)]


from enums.enums import MediusIdEnum, MediusEnum
from utils import utils

class PolicyResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

	@classmethod
	def build(self,
			message_id: bytes,
			callback_status: int,
			policy: str,
			end_of_list: int,
			):
		packet = [
			{'name': __name__},
			{'mediusid': MediusIdEnum.PolicyResponse},
			{'message_id': message_id},
			{'buf': utils.bytes_from_hex("000000")},
			{'callback_status': utils.int_to_bytes_little(4, callback_status)},
			{'policy': utils.str_to_bytes(policy, MediusEnum.POLICY_MAXLEN)},
			{'end_of_list': utils.int_to_bytes_little(4, end_of_list)}
		]
		return packet

class PolicyResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: PolicyResponseHandler')


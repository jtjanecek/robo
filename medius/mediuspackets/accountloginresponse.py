from enums.enums import MediusIdEnum
from enums.enums import MediusEnum
from utils import utils

class AccountLoginResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

	@classmethod
	def build(self,
			message_id: bytes,
			callback_status: int,
			account_id: int,
			account_type: int,
			world_id: int,
			mls_ip: str,
			mls_port: int,
			nat_ip: str,
			nat_port: int,
			session_key: bytes, 
			access_key: bytes
			):
		packet = [
			{'name': __name__},
			{'mediusid': MediusIdEnum.AccountLoginResponse},
			{'message_id': message_id},
			{'buf': utils.bytes_from_hex("000000")},
			{'callback_status': utils.int_to_bytes_little(4, callback_status)},
			{'account_id': utils.int_to_bytes_little(4, account_id)},
			{'account_type': utils.int_to_bytes_little(4, account_type)},
			{'world_id': utils.int_to_bytes_little(4, world_id)},
			{'unknown': utils.int_to_bytes_little(4, 1)},
			{'unknown': utils.int_to_bytes_little(4, 1)},
			{'mls_ip': utils.str_to_bytes(mls_ip, MediusEnum.BASIC_IP)},
			{'mls_port': utils.int_to_bytes_little(2, mls_port)},
			{'buf': utils.bytes_from_hex("000003000000")},
			{'mls_ip': utils.str_to_bytes(nat_ip, MediusEnum.BASIC_IP)},
			{'mls_port': utils.int_to_bytes_little(2, nat_port)},
			{'buf': utils.bytes_from_hex("00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")},
			{'session_key': session_key},
			{'buf': utils.bytes_from_hex("")},
			{'access_key': access_key},
			{'buf': utils.bytes_from_hex("0000")}
		]
		return packet

class AccountLoginResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: AccountLoginResponseHandler')

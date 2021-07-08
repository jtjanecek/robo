from enums.enums import MediusIdEnum, MediusEnum
from utils import utils

class GetMyClansResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

	@classmethod
	def build(self,
			message_id,
			callback_status,
			clan_id,
			app_id,
			clan_name,
			leader_account_id,
			leader_account_name,
			stats,
			clan_status,
			end_of_list
		):
		packet = [
			{'name': __name__},
			{'mediusid': MediusIdEnum.GetMyClansResponse},
			{'message_id': message_id},
			{'buf': utils.bytes_from_hex("000000")},
			{'callback_status': utils.int_to_bytes_little(4, callback_status)},
			{'clan_id': utils.int_to_bytes_little(4, clan_id)},
			{'app_id': utils.int_to_bytes_little(4, app_id)},
			{'clan_name': utils.str_to_bytes(clan_name, MediusEnum.CLANNAME_MAXLEN)},
			{'leader_account_id': utils.int_to_bytes_little(4, callback_status)},
			{'leader_account_name': utils.str_to_bytes(leader_account_name, MediusEnum.ACCOUNTNAME_MAXLEN)},
			{'stats': utils.str_to_bytes(stats, MediusEnum.CLANSTATS_MAXLEN)},
			{'clan_status': utils.int_to_bytes_little(4, clan_status)},
			{'end_of_list': utils.int_to_bytes_little(4, end_of_list)}
		]
		return packet

class GetMyClansResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: GetMyClansResponseHandler')


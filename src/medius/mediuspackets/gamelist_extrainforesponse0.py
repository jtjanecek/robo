from enums.enums import MediusIdEnum
from enums.enums import MediusEnum
from utils import utils

class GameList_ExtraInfoResponse0Serializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

	@classmethod
	def build(self,
			message_id,
			mls_world_id,
			callback_status,
			player_count,
			min_players,
			max_players,
			game_level,
			player_skill_level,
			rules_set,
			generic_field_1,
			generic_field_2,
			generic_field_3,
			world_security_level,
			world_status,
			game_host_type,
			game_name,
			game_stats,
			end_of_list
			):
		packet = [
			{'name': __name__},
			{'mediusid': MediusIdEnum.GameList_ExtraInfoResponse0},
			{'message_id': message_id},
			{'buf': utils.bytes_from_hex("000000")},
			{'callback_status': utils.int_to_bytes_little(4, callback_status)},
			{'mls_world_id': utils.int_to_bytes_little(4, mls_world_id)},
			{'player_count': utils.int_to_bytes_little(2, player_count)},
			{'min_players': utils.int_to_bytes_little(2, min_players)},
			{'max_players': utils.int_to_bytes_little(2, max_players)},
			{'buf': utils.bytes_from_hex("0000")},
			{'game_level': utils.int_to_bytes_little(4, game_level)},
			{'player_skill_level': utils.int_to_bytes_little(4, player_skill_level)},
			{'rules_set': utils.int_to_bytes_little(4, rules_set)},
			{'generic_field_1': utils.int_to_bytes_little(4, generic_field_1)},
			{'generic_field_2': utils.int_to_bytes_little(4, generic_field_2)},
			{'generic_field_3': utils.int_to_bytes_little(4, generic_field_3)},
			{'world_security_level': utils.int_to_bytes_little(4, world_security_level)},
			{'world_status': utils.int_to_bytes_little(4, world_status)},
			{'game_host_type': utils.int_to_bytes_little(4, game_host_type)},
			{'game_name': game_name},
			{'game_stats': game_stats},
			{'end_of_list': utils.int_to_bytes_little(4, end_of_list)}
		]
		return packet

class GameList_ExtraInfoResponse0Handler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: GameList_ExtraInfoResponse0Handler')

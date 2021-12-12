from enums.enums import MediusIdEnum
from utils import utils

class GameInfoResponse0Serializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

    @classmethod
    def build(self,
            message_id,
            callback_status,
            app_id,
            min_players,
            max_players,
            game_level,
            player_skill_level,
            player_count,
            stats,
            game_name,
            rules_set,
            generic_field_1,
            generic_field_2,
            generic_field_3,
            game_status,
            game_host_type
            ):
        packet = [
            {'name': __name__},
            {'mediusid': MediusIdEnum.GameInfoResponse0},
            {'message_id': message_id},
            {'buf': utils.hex_to_bytes("000000")},
            {'callback_status': utils.int_to_bytes_little(4, callback_status, signed=True)},
            {'app_id': utils.int_to_bytes_little(4, app_id)},
            {'min_players': utils.int_to_bytes_little(4, min_players)},
            {'max_players': utils.int_to_bytes_little(4, max_players)},
            {'game_level': utils.int_to_bytes_little(4, game_level)},
            {'player_skill_level': utils.int_to_bytes_little(4, player_skill_level)},
            {'player_count': utils.int_to_bytes_little(4, player_count)},
            {'stats': stats},
            {'game_name': game_name},
            {'rules_set': utils.int_to_bytes_little(4, rules_set)},
            {'generic_field_1': utils.int_to_bytes_little(4, generic_field_1)},
            {'generic_field_2': utils.int_to_bytes_little(4, generic_field_2)},
            {'generic_field_3': utils.int_to_bytes_little(4, generic_field_3)},
            {'game_status': utils.int_to_bytes_little(4, game_status)},
            {'game_host_type': utils.int_to_bytes_little(4, game_host_type)}
        ]
        return packet


class GameInfoResponse0Handler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: GameInfoResponse0Handler')


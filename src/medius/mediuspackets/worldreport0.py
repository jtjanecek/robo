from enums.enums import MediusEnum
from utils import utils
from datetime import datetime

class WorldReport0Serializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'session_key', 'n_bytes': MediusEnum.SESSIONKEY_MAXLEN, 'cast': None},
        {'name': 'buf', 'n_bytes': 3, 'cast': None},
        {'name': 'dme_world_id', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
        {'name': 'player_count', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
        {'name': 'game_name', 'n_bytes': MediusEnum.GAMENAME_MAXLEN, 'cast': None},
        {'name': 'game_stats', 'n_bytes': MediusEnum.GAMESTATS_MAXLEN, 'cast': None},
        {'name': 'min_players', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
        {'name': 'max_players', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
        {'name': 'game_level', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
        {'name': 'player_skill_level', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
        {'name': 'rules_set', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
        {'name': 'gen_field_1', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
        {'name': 'gen_field_2', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
        {'name': 'gen_field_3', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
        {'name': 'world_status', 'n_bytes': 4, 'cast': utils.bytes_to_int_little}
    ]


class WorldReport0Handler:
    def process(self, serialized, monolith, con):
        if serialized['world_status'] == 2:
            # Update the dme world as "active". And then update the game name
            game = monolith.get_client_manager().get_game(serialized['dme_world_id'])
            if (datetime.now().timestamp() - game._created_date) > 5:
                game.active()
        return []

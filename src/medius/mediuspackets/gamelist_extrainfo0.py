from enums.enums import MediusEnum, CallbackStatus, WorldSecurityLevelType
from utils import utils
from medius.mediuspackets.gamelist_extrainforesponse0 import GameList_ExtraInfoResponse0Serializer

class GameList_ExtraInfo0Serializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
        {'name': 'page_id', 'n_bytes': 2, 'cast': None},
        {'name': 'pag_size', 'n_bytes': 2, 'cast': None}
    ]

class GameList_ExtraInfo0Handler:
    def process(self, serialized, monolith, con):
        games = monolith.get_client_manager().get_games()

        packets = []

        player = monolith.get_client_manager().get_player_from_mls_con(con)
        lobby_world_id = player.get_mls_world_id()
        if lobby_world_id == 0:
            lobby_world_id = monolith.get_client_manager().get_channels()[0]['id']

        games = [game for game in games if game.get_created_info()['game_level'] == lobby_world_id]

        # We need to filter for the games that are only in the current players lobby world
        # This is stored in the "gameLevel" field

        for i in range(len(games)):
            game = games[i]
            serialized_game = game.get_created_info()

            if game.get_created_info()['game_password'][0] != 0x00:
                security_type = WorldSecurityLevelType.WORLD_SECURITY_PLAYER_PASSWORD
            else:
                security_type = WorldSecurityLevelType.WORLD_SECURITY_NONE


            packets.append(GameList_ExtraInfoResponse0Serializer.build(
                serialized['message_id'],
                game.get_dme_world_id(),
                CallbackStatus.SUCCESS,
                game.get_player_count(),
                serialized_game['min_players'],
                serialized_game['max_players'],
                serialized_game['game_level'],
                serialized_game['player_skill_level'],
                serialized_game['rules_set'],
                serialized_game['generic_field_1'],
                serialized_game['generic_field_2'],
                serialized_game['generic_field_3'],
                security_type,
                game.get_game_status(),
                serialized_game['game_host_type'],
                serialized_game['game_name'],
                game.get_stats(),
                int(i == (len(games) - 1))
            ))
        if (len(packets)) == 0:
            packets.append(GameList_ExtraInfoResponse0Serializer.build(
                serialized['message_id'],
                0,
                CallbackStatus.NO_RESULT,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                utils.str_to_bytes("", MediusEnum.GAMENAME_MAXLEN),
                utils.str_to_bytes("", MediusEnum.GAMESTATS_MAXLEN),
                1
            ))

        return packets

        

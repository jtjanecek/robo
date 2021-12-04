from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from medius.mediuspackets.gameworldplayerlistresponse import GameWorldPlayerListResponseSerializer

class GameWorldPlayerListSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
        {'name': 'session_key', 'n_bytes': MediusEnum.SESSIONKEY_MAXLEN, 'cast': None},
        {'name': 'buf', 'n_bytes': 2, 'cast': None},
        {'name': 'dme_world_id', 'n_bytes': 4, 'cast': utils.bytes_to_int_little}

    ]

class GameWorldPlayerListHandler:
    def process(self, serialized, monolith, con):

        client_manager = monolith.get_client_manager()
        game = client_manager.get_game(serialized['dme_world_id'])

        if game == None:
            return [GameWorldPlayerListResponseSerializer.build(
                serialized['message_id'],
                CallbackStatus.NO_RESULT,
                0,
                '',
                utils.str_to_bytes('',MediusEnum.ACCOUNTSTATS_MAXLEN),
                0,
                1
            )]

        packets = []
        players = game.get_players()
        for i in range(len(players)):
            player = players[i]
            packets.append(GameWorldPlayerListResponseSerializer.build(
                serialized['message_id'],
                CallbackStatus.SUCCESS,
                player['account_id'],
                player['username'],
                utils.bytes_from_hex(client_manager.get_player_stats(player['account_id'])),
                1, # connection class
                int(i == (len(players)-1))
            ))

        return packets

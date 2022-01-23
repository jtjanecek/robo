from enums.enums import MediusIdEnum
from enums.enums import MediusEnum
from utils import utils

class LadderList_ExtraInfoResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

    @classmethod
    def build(self,
            message_id,
            callback_status,
            ladder_position,
            ladder_stat,
            account_id,
            account_name,
            account_stats,
            player_status,
            lobby_world_id,
            game_world_id,
            lobby_name,
            game_name,
            end_of_list

            ):
        packet = [
            {'name': __name__},
            {'mediusid': MediusIdEnum.LadderList_ExtraInfoResponse},
            {'message_id': message_id},
            {'buf': utils.hex_to_bytes("000000")},
            {'callback_status': utils.int_to_bytes_little(4, callback_status)},
            {'ladder_position': utils.int_to_bytes_little(4, ladder_position)},
            {'ladder_stat': utils.int_to_bytes_little(4, ladder_stat)},
            {'account_id': utils.int_to_bytes_little(4, account_id)},
            {'account_name': utils.str_to_bytes(account_name, MediusEnum.ACCOUNTNAME_MAXLEN)},
            {'stats': utils.hex_to_bytes(account_stats)},
            {'player_status': utils.int_to_bytes_little(4, player_status)},
            {'lobby_world_id': utils.int_to_bytes_little(4, lobby_world_id)},
            {'game_world_id': utils.int_to_bytes_little(4, game_world_id)},
            {'lobby_name': utils.str_to_bytes(lobby_name, MediusEnum.LOBBYNAME_MAXLEN)},
            {'game_name': utils.str_to_bytes(game_name, MediusEnum.GAMENAME_MAXLEN)},
            {'end_of_list': utils.int_to_bytes_little(4, end_of_list)}
        ]
        return packet

class LadderList_ExtraInfoResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: LadderList_ExtraInfoResponseHandler')

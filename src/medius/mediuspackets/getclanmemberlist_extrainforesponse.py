from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from enums.enums import MediusIdEnum

class GetClanMemberList_ExtraInfoResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

    @classmethod
    def build(self,
            message_id,
            callback_status,
            account_id,
            account_name,
            account_stats,
            mediusPlayerStatus,
            medius_lobby_world_id,
            medius_game_world_id,
            lobby_name,
            game_name,
            ladderstat,
            ladderposition,
            totalrankings,
            end_of_list
            ):
        packet = [
            {'name': __name__},
            {'mediusid': MediusIdEnum.GetClanMemberList_ExtraInfoResponse},
            {'message_id': message_id},
            {'buf': utils.bytes_from_hex("000000")},
            {'callback_status': utils.int_to_bytes_little(4, callback_status, signed=True)},
            {'account_id': utils.int_to_bytes_little(4, account_id)},
            {'account_name': utils.str_to_bytes(account_name, MediusEnum.ACCOUNTNAME_MAXLEN)},
            {'account_stats': utils.str_to_bytes(account_stats, MediusEnum.ACCOUNTSTATS_MAXLEN) if account_stats == '' else utils.bytes_from_hex(account_stats)},
            {'player_status': utils.int_to_bytes_little(4, mediusPlayerStatus)},
            {'medius_lobby_world_id': utils.int_to_bytes_little(4, medius_lobby_world_id)},
            {'medius_game_world_id': utils.int_to_bytes_little(4, medius_game_world_id)},
            {'lobby_name': utils.str_to_bytes(lobby_name, MediusEnum.WORLDNAME_MAXLEN)},
            {'game_name': utils.str_to_bytes(game_name, MediusEnum.WORLDNAME_MAXLEN)},
            {'ladderstat': utils.int_to_bytes_little(4, ladderstat)},
            {'ladderposition': utils.int_to_bytes_little(4, ladderposition)},
            {'totalrankings': utils.int_to_bytes_little(4, totalrankings)},
            {'end_of_list': utils.int_to_bytes_little(4, end_of_list)},
        ]
        return packet


class GetClanMemberList_ExtraInfoResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: GetClanMemberList_ExtraInfoResponseHandler')


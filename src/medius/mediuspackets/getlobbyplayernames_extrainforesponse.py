from enums.enums import MediusIdEnum
from enums.enums import MediusEnum
from utils import utils

class GetLobbyPlayerNames_ExtraInfoResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

    @classmethod
    def build(self,
            message_id,
            callback_status,
            account_id,
            username,
            player_status,
            world_id,
            dme_world_id,
            lobby_name,
            game_name,
            end_of_list
            
            ):
        packet = [
            {'name': __name__},
            {'mediusid': MediusIdEnum.GetLobbyPlayerNames_ExtraInfoResponse},
            {'message_id': message_id},
            {'buf': utils.bytes_from_hex("000000")},
            {'callback_status': utils.int_to_bytes_little(4, callback_status)},
            {'account_id': utils.int_to_bytes_little(4, account_id)},
            {'username': utils.str_to_bytes(username, MediusEnum.ACCOUNTNAME_MAXLEN)},
            {'player_status': utils.int_to_bytes_little(4, player_status)},
            {'world_id': utils.int_to_bytes_little(4, world_id)},
            {'dme_world_id': utils.int_to_bytes_little(4, dme_world_id)},
            {'lobby_name': utils.str_to_bytes(lobby_name, MediusEnum.LOBBYNAME_MAXLEN)},
            {'game_name': game_name},
            {'end_of_list': utils.int_to_bytes_little(4, end_of_list)}
        ]
        return packet

class GetLobbyPlayerNames_ExtraInfoResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: GetLobbyPlayerNames_ExtraInfoResponseHandler')
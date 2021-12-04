from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from medius.mediuspackets.getlobbyplayernames_extrainforesponse import GetLobbyPlayerNames_ExtraInfoResponseSerializer


class GetLobbyPlayerNames_ExtraInfoSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
        {'name': 'buf', 'n_bytes': 3, 'cast': None},
        {'name': 'world_id', 'n_bytes': 4, 'cast': utils.bytes_to_int_little}
    ]


class GetLobbyPlayerNames_ExtraInfoHandler:
    def process(self, serialized, monolith, con):

        channel_name = [channel for channel in monolith.get_channels() if channel['id'] == serialized['world_id']][0]['name']
        players = monolith.get_client_manager().get_players_by_world(serialized['world_id'])
        packets = []

        for i, this_player in enumerate(players):
            packets.append(GetLobbyPlayerNames_ExtraInfoResponseSerializer.build(
                serialized['message_id'],
                CallbackStatus.SUCCESS,
                this_player.get_account_id(), # account_id
                this_player.get_username(), # account_name
                this_player.get_player_status(), # player_status
                serialized['world_id'], # lobby world_id
                this_player.get_dme_world_id(), # game world id
                channel_name, # lobby name
                utils.str_to_bytes("", MediusEnum.GAMENAME_MAXLEN), # game name # TODO
                int(i == (len(players)-1)) # end of list
            ))

        if len(players) == 0:
            packets.append(GetLobbyPlayerNames_ExtraInfoResponseSerializer.build(
                serialized['message_id'],
                CallbackStatus.NO_RESULT,
                0, # account_id
                utils.str_to_bytes("", MediusEnum.ACCOUNTNAME_MAXLEN), # account_name
                0, # player_status
                0, # lobby world_id
                0, # game world id
                channel_name, # lobby name
                utils.str_to_bytes("", MediusEnum.GAMENAME_MAXLEN), # game name # TODO
                1 # end of list
            ))

        return packets
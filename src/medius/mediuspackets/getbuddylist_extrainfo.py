from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from medius.mediuspackets.getbuddylist_extrainforesponse import GetBuddyList_ExtraInfoResponseSerializer

class GetBuddyList_ExtraInfoSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None}
    ]

class GetBuddyList_ExtraInfoHandler:
    def process(self, serialized, monolith, con):

        client_manager = monolith.get_client_manager()
        player = client_manager.get_player_from_mls_con(con)
        player_account_id = player.get_account_id()

        buddy_ids = client_manager.get_buddies(player_account_id)

        packets = []
        for i, buddy_id in enumerate(buddy_ids):

            player = client_manager.get_player(buddy_id)
            if player:
                username = player.get_username()
                player_status = player.get_player_status()
                dme_world_id = player.get_dme_world_id()
            else:
                username = client_manager.get_username(account_id=buddy_id)
                player_status = 0
                dme_world_id = 0

            packets.append(GetBuddyList_ExtraInfoResponseSerializer.build(
                serialized['message_id'],
                CallbackStatus.SUCCESS,
                buddy_id, # account_id
                username, # account_name
                player_status, # player_status
                123, # lobby world_id
                dme_world_id, # game world id
                '', # lobby name
                utils.str_to_bytes("", MediusEnum.GAMENAME_MAXLEN), # game name # TODO
                int(i == (len(buddy_ids)-1)) # end of list
            ))

        if len(buddy_ids) == 0:
            packets.append(GetBuddyList_ExtraInfoResponseSerializer.build(
                serialized['message_id'],
                CallbackStatus.NO_RESULT,
                0, # account_id
                '', # account_name
                0, # player_status
                123, # lobby world_id
                0, # game world id
                '', # lobby name
                utils.str_to_bytes("", MediusEnum.GAMENAME_MAXLEN), # game name # TODO
                1 # end of list
            ))


        return packets

        # return [GetBuddyList_ExtraInfoResponseSerializer.build(
        #     serialized['message_id'],
        #     "00000001000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001000000"
        # )]

        # 0AD20001D731000050000000000E00000000000000280D24000000000001000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001000000
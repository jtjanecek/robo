from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from medius.mediuspackets.getclanmemberlist_extrainforesponse import GetClanMemberList_ExtraInfoResponseSerializer

class GetClanMemberList_ExtraInfoSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
        {'name': 'buf', 'n_bytes': 3, 'cast': None},
        {'name': 'clan_id', 'n_bytes': 4, 'cast': utils.bytes_to_int_little}
    ]

class GetClanMemberList_ExtraInfoHandler:
    def process(self, serialized, monolith, con):

        client_manager = monolith.get_client_manager()
        clan_id = serialized['clan_id']

        clan_member_account_ids = client_manager.get_clan_member_account_ids(clan_id)

        if len(clan_member_account_ids) == 0:
            return [GetClanMemberList_ExtraInfoResponseSerializer.build(
                serialized['message_id'],
                CallbackStatus.NO_RESULT,
                0, # account id
                "", # account name
                "", # account stats
                0, # mediusPlayerStatus
                0, # mediuslobbyworldid
                0, # mediusgameworldid
                '', # lobbyname
                '', # gamename
                0,  # ladderstat
                0,  # ladderposition
                0,  # totalrankings
                1 # end of list
            )]

        packets = []
        for i, account_id in enumerate(clan_member_account_ids):

            username = client_manager.get_username(account_id=account_id)
            stats = client_manager.get_player_stats(account_id)

            packets.append(GetClanMemberList_ExtraInfoResponseSerializer.build(
                serialized['message_id'],
                CallbackStatus.SUCCESS,
                account_id,  # account id
                username,  # account name
                stats,  # account stats
                0,  # mediusPlayerStatus
                0,  # mediuslobbyworldid
                0,  # mediusgameworldid
                '',  # lobbyname
                '',  # gamename
                0,  # ladderstat
                0,  # ladderposition
                0,  # totalrankings
                1 if i+1 == len(clan_member_account_ids) else 0  # end of list
            ))
        return packets
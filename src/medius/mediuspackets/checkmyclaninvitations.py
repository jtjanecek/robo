from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from medius.mediuspackets.checkmyclaninvitationsresponse import CheckMyClanInvitationsResponseSerializer

class CheckMyClanInvitationsSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
    ]

class CheckMyClanInvitationsHandler:
    def process(self, serialized, monolith, con):

        client_manager = monolith.get_client_manager()
        player = client_manager.get_player_from_mls_con(con)
        account_id = player.get_account_id()

        clan_infos = client_manager.get_clan_invitations(account_id)
        print(clan_infos)
        if len(clan_infos) == 0:
            return [CheckMyClanInvitationsResponseSerializer.build(
                serialized['message_id'],
                CallbackStatus.NO_RESULT
            )]

        packets = []
        for i, clan_info in enumerate(clan_infos):

            leader_account_id = client_manager.get_clan_leader_account_id(clan_info['clan_id'])
            leader_account_name = client_manager.get_username(account_id=leader_account_id)

            clan_name = client_manager.get_clan_name(clan_info['clan_id'])

            packets.append(CheckMyClanInvitationsResponseSerializer.build(
                serialized['message_id'],
                CallbackStatus.SUCCESS,
                clan_info['clan_invitation_id'],
                clan_info['clan_id'],
                0, # response status,
                clan_name, # message.. but UYA uses the clan name...
                leader_account_id,
                leader_account_name,
                1 if i+1 == len(clan_infos) else 0  # end of list
            ))
        return packets






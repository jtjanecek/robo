from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from medius.mediuspackets.getclaninvitationssentresponse import GetClanInvitationsSentResponseSerializer

class GetClanInvitationsSentSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
    ]

class GetClanInvitationsSentHandler:
    def process(self, serialized, monolith, con):

        client_manager = monolith.get_client_manager()
        player = client_manager.get_player_from_mls_con(con)
        account_id = player.get_account_id()
        clan_id = client_manager.get_clan_id_from_account_id(account_id)

        clan_invs_sent = client_manager.get_clan_invitations_sent(clan_id)

        if len(clan_invs_sent) == 0:
            return [GetClanInvitationsSentResponseSerializer.build(
                serialized['message_id'],
                CallbackStatus.NO_RESULT,
                0, # account id
                '', # account_name
                '', # response message
                0, # response status
                0, # response_time
                1, # end of  list
            )]

        packets = []
        for i, account_data in enumerate(clan_invs_sent):
            username = client_manager.get_username(account_id=account_id)

            packets.append(GetClanInvitationsSentResponseSerializer.build(
                serialized['message_id'],
                CallbackStatus.NO_RESULT,
                account_data['account_id'], # account id
                username, # account_name
                account_data['response_msg'], # response message
                account_data['response_status'], # response status
                account_data['response_time'], # response_time
                1 if i+1 == len(clan_invs_sent) else 0  # end of list
            ))
        return packets

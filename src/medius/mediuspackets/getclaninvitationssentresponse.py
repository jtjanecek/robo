from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from enums.enums import MediusIdEnum

class GetClanInvitationsSentResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

    @classmethod
    def build(self,
              message_id,
              callback_status,
              account_id,
              username,
              response_msg,
              response_status,
              response_time,
              end_of_list
              ):
        packet = [
            {'name': __name__},
            {'mediusid': MediusIdEnum.GetClanInvitationsSentResponse},
            {'message_id': message_id},
            {'buf': utils.bytes_from_hex("000000")},
            {'callback_status': utils.int_to_bytes_little(4, callback_status, signed=True)},
            {'account_id': utils.int_to_bytes_little(4, account_id)},
            {'username': utils.str_to_bytes(username, MediusEnum.ACCOUNTNAME_MAXLEN)},
            {'response_msg': utils.str_to_bytes(username, MediusEnum.CLANMSG_MAXLEN)},
            {'response_status': utils.int_to_bytes_little(4, response_status)},
            {'response_time': utils.int_to_bytes_little(4, response_time)},
            {'end_of_list': utils.int_to_bytes_little(4, end_of_list)},
        ]
        return packet

class GetClanInvitationsSentResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: GetClanInvitationsSentResponseHandler')

from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from enums.enums import MediusIdEnum


class GetAllClanMessagesResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

    @classmethod
    def build(self,
              message_id,
              callback_status,
              clan_message_id,
              message,
              clan_message_status,
              end_of_list
              ):
        packet = [
            {'name': __name__},
            {'mediusid': MediusIdEnum.GetAllClanMessagesResponse},
            {'message_id': message_id},
            {'buf': utils.bytes_from_hex("000000")},
            {'callback_status': utils.int_to_bytes_little(4, callback_status, signed=True)},
            {'clan_id': utils.int_to_bytes_little(4, clan_message_id)},
            {'message': utils.str_to_bytes(message, MediusEnum.CLANMSG_MAXLEN)},
            {'clan_message_status': utils.int_to_bytes_little(4, clan_message_id)},
            {'end_of_list': utils.int_to_bytes_little(4, end_of_list)},
        ]
        return packet

class GetAllClanMessagesResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: GetAllClanMessagesResponseHandler')

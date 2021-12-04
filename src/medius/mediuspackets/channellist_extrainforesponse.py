from enums.enums import MediusIdEnum
from enums.enums import MediusEnum
from utils import utils

class ChannelList_ExtraInfoResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]


    @classmethod
    def build(self,
            message_id,
            callback_status,
            world_id,
            player_count,
            max_players,
            world_security_type,
            generic_field1,
            generic_field2,
            generic_field3,
            generic_field4,
            generic_field_filter,
            lobby_name,
            end_of_list):
        packet = [
            {'name': __name__},
            {'mediusid': MediusIdEnum.ChannelList_ExtraInfoResponse},
            {'message_id': message_id},
            {'buf': utils.bytes_from_hex("000000")},
            {'callback_status': utils.int_to_bytes_little(4, callback_status)},
            {'world_id': utils.int_to_bytes_little(4, world_id)},
            {'player_count': utils.int_to_bytes_little(2, player_count)},
            {'max_players': utils.int_to_bytes_little(2, max_players)},
            {'world_security_type': utils.int_to_bytes_little(4, world_security_type)},
            {'generic_field1': utils.int_to_bytes_little(4, generic_field1)},
            {'generic_field2': utils.int_to_bytes_little(4, generic_field2)},
            {'generic_field3': utils.int_to_bytes_little(4, generic_field3)},
            {'generic_field4': utils.int_to_bytes_little(4, generic_field4)},
            {'generic_field_filter': utils.int_to_bytes_little(4, generic_field_filter)},
            {'lobby_name': utils.str_to_bytes(lobby_name, MediusEnum.LOBBYNAME_MAXLEN)},
            {'end_of_list': utils.int_to_bytes_little(4, end_of_list)}
        ]
        return packet

class ChannelList_ExtraInfoResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: ChannelList_ExtraInfoResponseHandler')
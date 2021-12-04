from enums.enums import MediusIdEnum
from enums.enums import MediusEnum
from utils import utils

class SetLobbyWorldFilterResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

    @classmethod
    def build(self,
            message_id,
            callback_status,
            filter1,
            filter2,
            filter3,
            filter4,
            lobby_filter_type,
            lobby_filter_mask_level_type
            ):
        packet = [
            {'name': __name__},
            {'mediusid': MediusIdEnum.SetLobbyWorldFilterResponse},
            {'message_id': message_id},
            {'buf': utils.bytes_from_hex("000000")},
            {'callback_status': utils.int_to_bytes_little(4, callback_status)},
            {'filter1': filter1},
            {'filter2': filter2},
            {'filter3': filter3},
            {'filter4': filter4},
            {'lobby_filter_type': lobby_filter_type},
            {'lobby_filter_mask_level_type': lobby_filter_mask_level_type}        ]
        return packet


class SetLobbyWorldFilterResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: SetLobbyWorldFilterResponseHandler')


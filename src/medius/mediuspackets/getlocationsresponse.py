from enums.enums import MediusIdEnum, MediusEnum
from utils import utils

class GetLocationsResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

    @classmethod
    def build(self,
            message_id,
            location_id,
            location_name,
            callback_status,
            end_of_list
        ):
        packet = [
            {'name': __name__},
            {'mediusid': MediusIdEnum.GetLocationsResponse},
            {'message_id': message_id},
            {'buf': utils.hex_to_bytes("000000")},
            {'location_id': utils.int_to_bytes_little(4, location_id)},
            {'location_name': utils.str_to_bytes(location_name, MediusEnum.LOCATIONNAME_MAXLEN)},
            {'callback_status': utils.int_to_bytes_little(4, callback_status)},
            {'end_of_list': utils.int_to_bytes_little(4, end_of_list)}
        ]
        return packet

class GetLocationsResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: GetLocationsResponseHandler')

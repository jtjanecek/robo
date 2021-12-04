from medius.mediuspackets.getlocationsresponse import GetLocationsResponseSerializer
from utils import utils
from enums.enums import CallbackStatus, MediusEnum

class GetLocationsSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
        {'name': 'session_key', 'n_bytes': MediusEnum.SESSIONKEY_MAXLEN, 'cast': None}
    ]

class GetLocationsHandler:
    def process(self, serialized, monolith, con):
        packets = []

        locations = monolith.get_locations()
        for i in range(len(locations)):
            packets.append(
                GetLocationsResponseSerializer.build(
                    serialized['message_id'],
                    locations[i]['id'],
                    locations[i]['name'],
                    CallbackStatus.SUCCESS,
                    int(i == (len(locations)-1))
            ))
        return packets
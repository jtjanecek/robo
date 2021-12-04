from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from medius.mediuspackets.setlobbyworldfilterresponse import SetLobbyWorldFilterResponseSerializer

class SetLobbyWorldFilterSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
        {'name': 'buf', 'n_bytes': 3, 'cast': None},
        {'name': 'filter1', 'n_bytes': 4, 'cast': None},
        {'name': 'filter2', 'n_bytes': 4, 'cast': None},
        {'name': 'filter3', 'n_bytes': 4, 'cast': None},
        {'name': 'filter4', 'n_bytes': 4, 'cast': None},
        {'name': 'lobby_filter_type', 'n_bytes': 4, 'cast': None},
        {'name': 'lobby_filter_mask_level_type', 'n_bytes': 4, 'cast': None}
    ]

class SetLobbyWorldFilterHandler:
    def process(self, serialized, monolith, con):
        return [SetLobbyWorldFilterResponseSerializer.build(
                serialized['message_id'],
                CallbackStatus.SUCCESS,
                serialized['filter1'],
                serialized['filter2'],
                serialized['filter3'],
                serialized['filter4'],
                serialized['lobby_filter_type'],
                serialized['lobby_filter_mask_level_type']
            )]
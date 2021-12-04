from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from medius.mediuspackets.setlocalizationparamsresponse import SetLocalizationParamsResponseSerializer

class SetLocalizationParamsSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None}
    ]

class SetLocalizationParamsHandler:
    def process(self, serialized, monolith, con):
        return [SetLocalizationParamsResponseSerializer.build(serialized['message_id'], CallbackStatus.SUCCESS)]

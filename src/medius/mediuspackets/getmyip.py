from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from medius.mediuspackets.getmyipresponse import GetMyIPResponseSerializer

class GetMyIPSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None}
    ]

class GetMyIPHandler:
    def process(self, serialized, monolith, con):

        addr = con.addr

        return [GetMyIPResponseSerializer.build(
            serialized['message_id'],
            addr,
            CallbackStatus.SUCCESS
        )]

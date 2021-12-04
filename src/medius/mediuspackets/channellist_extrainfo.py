
from utils import utils

class ChannelList_ExtraInfoSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class ChannelList_ExtraInfoHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: ChannelList_ExtraInfoHandler')


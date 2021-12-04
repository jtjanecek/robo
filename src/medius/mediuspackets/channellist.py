
from utils import utils

class ChannelListSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class ChannelListHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: ChannelListHandler')


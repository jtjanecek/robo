
from utils import utils

class PlayerReportSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class PlayerReportHandler:
    def process(self, serialized, monolith, con):
        return []

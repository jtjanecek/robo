
from utils import utils

class ClientAppBroadcastSerializer:
    data_dict = [
        {'name': 'rtid', 'n_bytes': 1, 'cast': None},
        {'name': 'len', 'n_bytes': 2, 'cast': utils.bytes_to_int_little},
        {'name': 'data', 'n_bytes': None, 'cast': None}
    ]

    def serialize(self, data: bytes):
        return utils.serialize(data, self.data_dict, __name__)

class ClientAppBroadcastHandler:
    def process(self, serialized, monolith, con):


        # Con has to be either dmetcp or dmeudp
        if con.server_name == 'dmetcp':
            monolith.get_client_manager().dmetcp_broadcast(con, serialized['data'])
        elif con.server_name == 'dmeudp':
            monolith.get_client_manager().dmeudp_broadcast(con, serialized['data'])
        else:
            raise Exception('Unimplemented Handler: ClientAppBroadcastHandler')

        return []

from enums.enums import MediusIdEnum
from enums.enums import MediusEnum
from utils import utils

class JoinGameResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

    @classmethod
    def build(self,
            message_id,
            callback_status,
            game_host_type,
            net_connection_type,
            dme_ip_type,
            dmetcp_ip,
            dmetcp_port,
            nat_ip_type,
            nat_ip,
            nat_port,
            dme_world_id,
            encryption_key,
            session_key,
            access_key
        ):
        packet = [
            {'name': __name__},
            {'mediusid': MediusIdEnum.JoinGameResponse},
            {'message_id': message_id},
            {'buf': utils.hex_to_bytes("000000")},
            {'callback_status': utils.int_to_bytes_little(4, callback_status, signed=True)},
            {'game_host_type': utils.int_to_bytes_little(4, game_host_type)},
            {'net_connection_type': utils.int_to_bytes_little(4, net_connection_type)},

            {'dme_ip_type': utils.int_to_bytes_little(4, dme_ip_type)},
            {'dmetcp_ip': utils.str_to_bytes(dmetcp_ip, MediusEnum.BASIC_IP)},
            {'dmetcp_port': utils.int_to_bytes_little(4, dmetcp_port)},

            {'nat_ip_type': utils.int_to_bytes_little(4, nat_ip_type)},
            {'nat_ip': utils.str_to_bytes(nat_ip, MediusEnum.BASIC_IP)},
            {'nat_port': utils.int_to_bytes_little(4, nat_port)},

            {'dme_world_id': utils.int_to_bytes_little(4, dme_world_id)},
            {'encryption_key': encryption_key},
            {'session_key': session_key},
            {'access_key': access_key}
        ]
        return packet

class JoinGameResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: JoinGameResponseHandler')


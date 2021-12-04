from enums.enums import MediusIdEnum
from enums.enums import MediusEnum
from utils import utils

class JoinChannelResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

    @classmethod
    def build(self,
            message_id: bytes,
            callback_status: int,
            net_connection_type_1: int,
            net_connection_type_2: int,
            mls_ip: str,
            mls_port: int,
            world_id: int,
            session_key: bytes, 
            access_key: bytes
            ):
        packet = [
            {'name': __name__},
            {'mediusid': MediusIdEnum.JoinChannelResponse},
            {'message_id': message_id},
            {'buf': utils.bytes_from_hex("000000")},
            {'callback_status': utils.int_to_bytes_little(4, callback_status)},
            {'net_connection_type_1': utils.int_to_bytes_little(4, net_connection_type_1)},
            {'net_connection_type_2': utils.int_to_bytes_little(4, net_connection_type_2)},
            {'mls_ip': utils.str_to_bytes(mls_ip, MediusEnum.BASIC_IP)},
            {'mls_port': utils.int_to_bytes_little(2, mls_port)},
            {'buf': utils.bytes_from_hex("00000000000000000000000000000000000000000000FFFFFFFF")},
            {'world_id': utils.int_to_bytes_little(4, world_id)},
            {'buf': utils.bytes_from_hex("00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")},
            {'session_key': session_key},
            {'access_key': access_key},
            {'buf': utils.bytes_from_hex("0000")}
        ]
        return packet

class JoinChannelResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: JoinChannelResponseHandler')

'''

            outputStream.write(messageId);
            outputStream.write(Utils.hexStringToByteArray("000000")); // Padding
            outputStream.write(callbackStatus);

            outputStream.write(Utils.intToBytesLittle(NetConnectionType.NET_CONNECTION_TYPE_CLIENT_SERVER_TCP.getValue())); // net connection type (int/little endian)

            outputStream.write(Utils.intToBytesLittle(NetAddressType.NET_ADDRESS_TYPE_EXTERNAL.getValue())); // net address type (int/little endian)

            outputStream.write(ipAddr); // ip address
            outputStream.write(zeroTrail); // zero padding for ip address

            outputStream.write(Utils.shortToBytesLittle(port)); // port

            // ???
            outputStream.write(Utils.hexStringToByteArray("00000000000000000000000000000000000000000000ffffffff"));

            // world id
            outputStream.write(worldId);

            // RSA_KEY 64
            outputStream.write(Utils.hexStringToByteArray("00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")); // RSA_KEY 64

            outputStream.write(Utils.hexStringToByteArray("3333323837000000000000000000000000")); // aSessionKey

            // outputStream.write(Utils.hexStringToByteArray("782B6F2F532F71443453633243364B4E"));
            // aAccessKey
            outputStream.write(mlsToken.getBytes()); // aAccessKey
            outputStream.write(Utils.hexStringToByteArray("0000"));
'''
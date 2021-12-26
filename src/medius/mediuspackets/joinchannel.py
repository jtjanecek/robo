from enums.enums import MediusEnum, CallbackStatus, NetConnectionType, NetAddressType
from utils import utils
from medius.mediuspackets.joinchannelresponse import JoinChannelResponseSerializer


class JoinChannelSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
        {'name': 'session_key', 'n_bytes': MediusEnum.SESSIONKEY_MAXLEN, 'cast': None},
        {'name': 'buf', 'n_bytes': 2, 'cast': None},
        {'name': 'world_id', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
        {'name': 'lobby_channel_password', 'n_bytes': MediusEnum.LOBBYPASSWORD_MAXLEN, 'cast': None}
    ]

class JoinChannelHandler:
    def process(self, serialized, monolith, con):
        return [JoinChannelResponseSerializer.build(
            serialized['message_id'],
            CallbackStatus.SUCCESS,
            NetConnectionType.NET_CONNECTION_TYPE_CLIENT_SERVER_TCP,
            NetAddressType.NET_ADDRESS_TYPE_EXTERNAL,
            monolith.get_mls_ip(),
            monolith.get_mls_port(),
            serialized['world_id'],
            serialized['session_key'],
            monolith.get_client_manager().generate_access_key()
        )]

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
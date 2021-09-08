from utils import utils
from crypto.rsa import RSA
from crypto.rc4 import RC4
from medius.rtpackets.servercryptkeypeer import ServerCryptkeyPeerSerializer

class ClientCryptkeyPublicSerializer:
	data_dict = [
		{'name': 'rtid', 'n_bytes': 1, 'cast': None},
		{'name': 'len', 'n_bytes': 2, 'cast': utils.bytes_to_int_little},
		{'name': 'rsa_key', 'n_bytes': 64, 'cast': utils.bytes_to_int_little}
	]

	def serialize(self, data: bytes):
		return utils.serialize(data, self.data_dict, __name__)

class ClientCryptkeyPublicHandler:
	def process(self, serialized, monolith, con):
		client_rsa = RSA(n=serialized['rsa_key'],e=17)
	
		con.set_rsa(client_rsa)

		rc4_key = utils.generate_rc4_key()

		client_rc4 = RC4(rc4_key)
		con.set_rc4(client_rc4)

		return [ServerCryptkeyPeerSerializer.build(rc4_key)]
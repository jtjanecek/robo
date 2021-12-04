import json
import os
import math
import hashlib
from enums.enums import CipherContext
from utils import utils

class RSA:
    def __init__(self, n=None, e=None, json_file='ps2.json'):
        if n==None and e==None:
            with open(os.path.join('crypto', json_file)) as f:
                keys = json.loads(f.read())[0]
            self._p = int(keys['p'])
            self._q = int(keys['q'])
            self._n = int(keys['n'])
            self._e = int(keys['e'])
            self._d = int(keys['d'])
        else:
            self._n = n
            self._e = e


    def decrypt(self, data: bytes, hash: bytes):
        intlist = int.from_bytes(data, 'little')

        # c^d mod n
        z = pow(intlist, self._d, self._n)
        z += self._n
        try:
            bytesDecrypted = z.to_bytes(len(data), 'little')
        except OverflowError:
            z -= self._n
            bytesDecrypted = z.to_bytes(len(data), 'little')
        print(utils.bytes_to_hex(bytesDecrypted))
        return bytesDecrypted

    def encrypt(self, data: bytes) -> bytes:
        rtid = data[0] | 0x80
        length = data[1:3]
        data_to_encrypt = data[3:]

        context = CipherContext.RSA_AUTH;
        
        digest = hashlib.sha1()
        digest.update(data_to_encrypt)
        rthash = digest.digest()[0:4]
        contextFlip = (rthash[3] & 0x1F) | ((context & 7) << 5)
        rthash = bytes([rthash[0], rthash[1], rthash[2], contextFlip])

        cipher = pow(utils.bytes_to_int_little(data_to_encrypt), self._e, self._n)
        cipher_bytes = utils.int_to_bytes_little(64, cipher)

        return bytes([rtid] + list(length) + list(rthash) + list(cipher_bytes))


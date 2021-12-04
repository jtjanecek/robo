import json
import os
import math
import hashlib
from enums.enums import CipherContext
from utils import utils

class RC4:
    def __init__(self, key, context=CipherContext.RC_CLIENT_SESSION):
        self._key = key
        self._context = context

        self._x = 0
        self._y = 0
        self._engine = [hex(i) for i in range(255,-1,-1)] # 256 -> 0


    def set_key(self, key, chash):
        self._x = 0
        self._y = 0

        key_index = 0
        li = 0
        cipher_index = 0
        id_index = 0

        self._engine = [i for i in range(255,-1,-1)] # 256 -> 0

        # apply hash
        v1 = chash[id_index]
        id_index = (id_index+1)&3
        temp = self._engine[cipher_index]
        v1 += li
        li = (temp+v1) & 0xFF

        self._engine[cipher_index] = self._engine[li];
        self._engine[li] = temp;
        cipher_index = (cipher_index + 5) & 0xFF

        while (cipher_index != 0):
            v1 = chash[id_index]
            id_index = (id_index+1)&3
            temp = self._engine[cipher_index]
            v1 += li
            li = (temp+v1) & 0xFF

            self._engine[cipher_index] = self._engine[li];
            self._engine[li] = temp;
            cipher_index = (cipher_index + 5) & 0xFF

        key_index = 0
        li = 0
        cipher_index = 0
        id_index = 0

        # apply key
        key_byte = key[key_index]
        key_byte += li
        key_index += 1
        key_index &= 0x3F
        cipher_byte = self._engine[cipher_index]
        cipher_value = cipher_byte & 0xFF
        cipher_byte += key_byte
        li = cipher_byte & 0xFF
        t0 = self._engine[li]
        self._engine[cipher_index] = t0
        self._engine[li] = cipher_value
        cipher_index += 3
        cipher_index &= 0xFF

        while (cipher_index != 0):
            key_byte = key[key_index]
            key_byte += li
            key_index += 1
            key_index &= 0x3F
            cipher_byte = self._engine[cipher_index]
            cipher_value = cipher_byte & 0xFF
            cipher_byte += key_byte
            li = cipher_byte & 0xFF
            t0 = self._engine[li]
            self._engine[cipher_index] = t0
            self._engine[li] = cipher_value
            cipher_index += 3
            cipher_index &= 0xFF

    def _decrypt(self, data: bytes):
        inOff, outOff = 0, 0

        output = [0] * len(data)
        for i in range(len(data)):
            self._y = (self._y + 5) & 0xFF
            v0 = self._engine[self._y]
            a2 = v0 & 0xFF
            v0 += self._x
            self._x = v0 & 0xFF
            v0 = self._engine[self._x]
            self._engine[self._y] = v0 & 0xFF
            self._engine[self._x] = a2
            a0 = data[i+inOff]
            v0 += a2
            v0 &= 0xFF
            v1 = self._engine[v0] & 0xFf
            a0 ^= v1
            output[i+outOff] = a0 & 0xFF
            v1 = self._engine[a0 & 0xFF] + self._x
            self._x = v1 & 0xFF
        return bytes(output)


    def decrypt(self, data: bytes, chash: bytes):

        self.set_key(self._key, chash)
        result = self._decrypt(data)

        return result

    def _encrypt(self, payload:bytes):
        result = [0] * len(payload)
        for i in range(len(payload)):
            self._x = (self._x + 5) & 0xFF
            self._y = (self._y + self._engine[self._x]) & 0xFF

            temp = self._engine[self._x]
            self._engine[self._x] = self._engine[self._y]
            self._engine[self._y] = temp
            
            result[i] = (payload[i] & 0xFF) ^ (self._engine[((self._engine[self._x] & 0xFF) + (self._engine[self._y] & 0xFF)) & 0xFF])

            self._y = (self._engine[payload[i] & 0xFF] + self._y) & 0xFF

        return bytes(result)

    def encrypt(self, data: bytes) -> bytes:
        rtid = data[0] | 0x80
        length = data[1:3]
        payload = data[3:]

        context = self._context
        
        digest = hashlib.sha1()
        digest.update(payload)
        rthash = digest.digest()[0:4]
        contextFlip = (rthash[3] & 0x1F) | ((context & 7) << 5)
        rthash = bytes([rthash[0], rthash[1], rthash[2], contextFlip])

        self.set_key(self._key, rthash)

        cipher = self._encrypt(payload)

        return b'' + bytes([rtid]) + length + rthash + cipher

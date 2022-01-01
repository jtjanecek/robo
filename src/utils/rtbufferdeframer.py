from utils import utils
import numpy as np

class RtBuffer():
    def __init__(self):
        self._buffer = [0] * 2048

        self._cursor = 0
        self._encrypted = False

    def process(self, b): 
        self._buffer[self._cursor] = b

        if (self._cursor == 0):
            # Check if id is > 0x80
            self._encrypted = (self._buffer[0] & 0xFF) >= 128

        self._cursor += 1

    def is_full(self) -> bool:
        if (self._cursor < 3):
            return False
        return self._cursor == self.get_full_length()

    def get_full_length(self) -> int:
        length = 1 + 2 + utils.bytes_to_int_little(self._buffer[1:3])
        if (self._encrypted): # hash
            length += 4
        return length

    def to_bytes(self) -> bytes:
        return bytes(self._buffer[0:self.get_full_length()])

    def clear(self):
        self._cursor = 0

class RtBufferDeframer():
    def __init__(self):
        self._rtbuffer = RtBuffer()

    def deframe(self, data: bytes):
        results = []
        for b in data:
            self._rtbuffer.process(b)

            if self._rtbuffer.is_full():
                results.append(self._rtbuffer.to_bytes())
                self._rtbuffer.clear()
        return results

    @classmethod
    def basic_deframe(self, data: [bytes]):
        deframer = RtBufferDeframer()
        return deframer.deframe(data)

 
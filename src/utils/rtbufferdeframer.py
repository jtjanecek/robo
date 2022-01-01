from utils import utils
import numpy as np
from numba import jit


@jit(nopython=True)
def process(input_buf, data):

    results = []
    buf = None

    if input_buf is not None:
        data = np.concatenate((input_buf,data))

    while True:
        len_bytes = data[1:3] # Reverse it
        len_bytes = len_bytes[0] + (len_bytes[1]*16*16) # calculate length of packet

        packet_length = 1 + 2 + len_bytes
        
        if (data[0] & 0xFF) >= 128: # Encrypted. So we need to add the hash to the packet length
            packet_length += 4

        if packet_length == data.size: # Perfect fit
            results.append(data)
            return buf, results
        elif packet_length > data.size: # This happens when the packet is cut-off
            buf = data
            return buf, results
        elif packet_length < data.size: # Multiple packets here
            results.append(data[0:packet_length])
            data = data[packet_length:]
        else:
            raise Exception("Unknown error!")

    return buf, results


class RtBufferDeframer():
    def __init__(self):
        self._buffer = None

    def deframe(self, data: bytes):
        data = np.frombuffer(data, dtype=np.uint8, count=-1)
        buf, results = process(self._buffer, data)
        self._buffer = buf
        results = [result.tobytes() for result in results]
        return results


    @classmethod
    def basic_deframe(self, data: bytes):
        deframer = RtBufferDeframer()
        return deframer.deframe(data)


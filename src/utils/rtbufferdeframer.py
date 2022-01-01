from utils import utils
import numpy as np

class RtBufferDeframer():
    def __init__(self):
        self._buffer = None

    def deframe(self, data: bytes):
        data = np.frombuffer(data, dtype=np.uint8, count=-1)

        if self._buffer is not None:
            data = np.concatenate((self._buffer,data), axis=None)
            self._buffer = None

        results = []

        while True:

            packet_length = 1 + 2 + utils.bytes_to_int_little(data[1:3])
            if (data[0] & 0xFF) >= 128: # Encrypted. So we need to add the hash to the packet length
                packet_length += 4

            if packet_length == data.size: # Perfect fit
                results.append(data.tobytes())
                return results
            elif packet_length > data.size: # This happens when the packet is cut-off
                self._buffer = data
                return results
            elif packet_length < data.size: # Multiple packets here
                results.append(data[0:packet_length].tobytes())
                data = data[packet_length:]
            else:
                raise Exception("Unknown error!")

        return results

    @classmethod
    def basic_deframe(self, data: bytes):
        deframer = RtBufferDeframer()
        return deframer.deframe(data)


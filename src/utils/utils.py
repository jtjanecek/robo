import traceback
from collections import deque
from enums.enums import MediusEnum
from hashlib import sha512

def rtpacket_to_bytes(packet: list):
    '''
    Create a byte array from an rt id and the 
    byte arrays that go into that payload. 

    If an arg is a dict, it is interpreted as a 
    medius packet, and will be consolidated into
    the packet

    '''

    name = packet.pop(0)
    rtid = packet.pop(0)['rtid']
    result = b''
    for arg in packet:
        arg = list(arg.values())[0]
        if type(arg) == int:
            result += bytes([arg])
        # Medius internal packet
        elif type(arg) == list:
            arg.pop(0) # Remove the name for the mediuspacket
            for mediusarg in arg:
                mediusvalue = list(mediusarg.values())[0]
                if type(mediusvalue) == int:
                    result += bytes([mediusvalue])
                else:
                    result += bytes(mediusvalue)
        else:
            result += bytes(arg)
    return bytes([rtid]) + int_to_bytes_little(2, len(result)) + result

def serialize(data: bytes, data_dict: [dict], name: str) -> dict:
    '''Serialize the byte array based on the data dictionary
    '''
    byteList = deque(data)
    results = {'packet': name}
    try:
        for pair in data_dict:
            if len(byteList) <= 0:
                break
            thisBytes = []

            if pair['n_bytes'] == None:
                while len(byteList) != 0:
                    thisBytes.append(byteList.popleft())
            else:
                for _ in range(pair['n_bytes']):
                    thisBytes.append(byteList.popleft())

            if pair['cast'] == None:
                results[pair['name']] = bytes(thisBytes)
            else:
                results[pair['name']] = pair['cast'](bytes(thisBytes))
    except:
        print("ERROR SERIALIZING: " + data.hex().upper())
        traceback.print_exc()
    return results

def flatten(l):
    results = []
    for sublist in l:
        for s in sublist:
            results.append(s)
    return results


def generate_rc4_key() -> bytes:
    return hex_to_bytes("E7477438E0234BB8196D574F09337BE7A72971628C551C3373A68BE7F1F108181EAAC2419AFA7583215E79775E9D6DBC8D442545EF396F29C6294C69FC97E177")

def generate_server_rc4_key() -> bytes:
    return hex_to_bytes('59F5AECD5CCD444855688FAE31C271C402BDB6C090843B693644840675FBCD4DD82C6011FE3CDEDEF949B0A32DFBAE6E086538055C7B7E5C9A891357E41C8C07')

def format_rt_message(rtid, *args) -> bytes:
    # DON"T USE IN FUTURE
    result = b''
    for arg in args:
        if type(arg) == int:
            result += bytes([arg])
        else:
            result += bytes(arg)
    return bytes([rtid]) + int_to_bytes_little(2, len(result)) + result

def pad_str(s, size) -> str:
    return s.ljust(size,'\0')

def check_username_valid(username: str) -> bool:
    # First or last characters are spaces
    if username[0] == ' ' or username[-1] == ' ':
        return False

    # Ensure length > 1
    if len(username) == 1:
        return False

    # Multiple spaces together aren't supported on UYA keyboard
    if '  ' in username:
        return False

    for c in username:
        if ord(c) < 32 or ord(c) > 126 or ord(c) == 96: # Tilda character not on uya keyboard
            return False
    return True

def check_ctag_valid(ctag: bytes):
    ctag_str = bytes_to_str(ctag)

    # First or last characters are spaces
    if ctag_str[0] == ' ' or ctag_str[-1] == ' ':
        return False

    # Multiple spaces together aren't supported on UYA keyboard
    if '  ' in ctag_str:
        return False

    for c in ctag_str:
        if ord(c) > 7 and ord(c) < 15: # Color codes
            continue
        if ord(c) > 15 and ord(c) < 27: # Buttons
            continue
        if ord(c) < 32 or ord(c) > 126 or ord(c) == 96: # Tilda character not on uya keyboard
            return False
    return True

############################ Conversions

def sha512_encrypt(data):
    password = bytes_to_str(data)
    sha = sha512()
    sha.update(password.encode())
    encrypted_password = bytes_to_hex(sha.digest())
    return encrypted_password

def bytes_to_int_little(data):
    return int.from_bytes(data, byteorder='little')

def bytes_to_int_big(data):
    return int.from_bytes(data, byteorder='big')

def int_to_bytes_little(bytelength, data, signed=False):
    return data.to_bytes(bytelength, 'little', signed=signed)

def int_to_bytes_big(bytelength, data):
    return data.to_bytes(bytelength, 'big')

def bytes_to_hex(data:bytes):
    return data.hex().upper()

def hex_to_bytes(hex:str):
    return bytes(bytearray.fromhex(hex))

def bytes_to_str(data: bytes) -> str:
    res = ''
    for b in data:
        if b == 0x00:
            return res
        res += chr(b)
    return res
    
def str_to_bytes(data: str, length: int) -> bytes:
    str_bytes = data
    assert(length > len(data))
    while (len(str_bytes) != length):
        str_bytes += '\0'
    return str_bytes.encode()


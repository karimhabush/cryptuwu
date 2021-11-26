import  base64
from typing import ByteString
from Crypto.Random import get_random_bytes

def randgen(numbytes,algo):
    key = get_random_bytes(numbytes) # generate a random key of numbytes bytes
    if algo=='base64':
        return base64.b64encode(key).decode("utf-8")
    if algo=='hex':
        return key.hex()
    else:
        return 'error : unexistant algorithm'


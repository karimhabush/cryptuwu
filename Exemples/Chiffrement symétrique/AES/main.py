from hashlib import md5
from base64 import b64decode
from base64 import b64encode
from Crypto.Cipher import AES


# Padding for the input string to fix block sizes to 16 bytes
BLOCK_SIZE = 16  # Bytes
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

def encrypt(raw):
    password = input('Password..: ')
    key = md5(password.encode('utf8')).hexdigest()
    raw = pad(raw)
    cipher = AES.new(key.encode("utf8"), AES.MODE_ECB)
    return b64encode(cipher.encrypt(raw.encode('utf8')))

def decrypt(enc):
    password = input('Password..: ')
    key = md5(password.encode('utf8')).hexdigest()
    enc = b64decode(enc)
    cipher = AES.new(key.encode("utf8"), AES.MODE_ECB)
    return unpad(cipher.decrypt(enc)).decode('utf8')



msg = input('Message...: ')
print(encrypt(msg))

from hashlib import md5
from base64 import b64decode
from base64 import b64encode
from Crypto.Cipher import AES


# Padding for the input string to fix block sizes to 16 bytes
BLOCK_SIZE = 16  # Bytes
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

def encrypt(filepath,keypath):
    try:
        keyfile=open(keypath,'rb')
        key = keyfile.read()
        f_input = open(filepath, 'rb') #open binary file in read mode
        raw = f_input.read()
        raw = pad(raw.decode('utf8'))
        cipher = AES.new(key, AES.MODE_ECB)
        f_output = open(filepath+".enc","w")
        f_output.write(b64encode(cipher.encrypt(raw.encode('utf8'))).decode("utf-8"))
        keyfile.close()
        f_input.close()
        f_output.close()
    except Exception as e: 
        print(str(e))

def decrypt(filepath,keypath):
    try:
        keyfile=open(keypath,'rb')
        key = keyfile.read()
        f_input = open(filepath, 'rb') #open binary file in read mode
        enc = f_input.read()
        enc = b64decode(enc)
        cipher = AES.new(key, AES.MODE_ECB)
        out = unpad(cipher.decrypt(enc)).decode('utf8')
        f_output = open(filepath+".dec","w")
        f_output.write(out)
        keyfile.close()
        f_input.close()
        f_output.close()
    except Exception as e:
        print(str(e))


from os import write
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
from base64 import b64decode
from base64 import b64encode

def rsa_encrypt(filepath,publickey):
    try:
        f_input = open(filepath, 'rb') #open binary file in read mode
        raw = f_input.read()
        file_out = open(filepath+"enc", "wb")
        pubkey = RSA.import_key(open(publickey).read())
        # Encrypt the data with the public RSA key
        cipher_rsa = PKCS1_OAEP.new(pubkey)
        file_out.write((cipher_rsa.encrypt(raw)))
        file_out.close()
    except Exception as e:
        print(str(e))

def rsa_decrypt(filepath,priv_path):
    try:
        file_in = open(filepath, "rb")
        file_out = open(filepath+"dec", "wb")
        private_key = RSA.import_key(open(priv_path).read())
        ciphertext = file_in.read()

        # Decrypt the cipher with the private RSA key
        cipher_rsa = PKCS1_OAEP.new(private_key)
        output = cipher_rsa.decrypt(ciphertext)
        file_out.write(output)
    except Exception as e:
        print(str(e))

rsa_decrypt('rsaenc.enc','private.pem')
from Crypto.Cipher import DES3 
from Crypto.Random import get_random_bytes
from base64 import b64decode
from base64 import b64encode

while True : 
    try : 
        key = DES3.adjust_key_parity(get_random_bytes(24))
        break
    except ValueError :
        pass 

def encrypt(filepath):
    try : 
        f_input = open(filepath, 'rb') #open binary file in read mode
        f_read = f_input.read()
        cipher = DES3.new(key, DES3.MODE_EAX)
        nonce = cipher.nonce
        ciphertext = cipher.encrypt(f_read)
        f_output_enc = open(filepath+".enc","w")
        f_output_nonce = open("nonce","wb")
        f_output_key = open("key","wb")

        f_output_enc.write(b64encode(ciphertext).decode("utf8"))
        f_output_nonce.write(nonce)
        f_output_key.write(key)

        f_input.close()
        f_output_nonce.close()
        f_output_key.close()
        f_output_enc.close()
    except Exception as e: 
        print(str(e))

def decrypt(cipherfile,nonce,key):
    try : 
        f_input_cipher = open(cipherfile, 'rb') #open binary file in read mode
        f_input_nonce = open(nonce, 'rb') #open binary file in read mode
        f_input_key = open(key, 'rb') #open binary file in read mode

        f_read_cipher = f_input_cipher.read()
        f_read_nonce = f_input_nonce.read()
        f_read_key = f_input_key.read()

        cipher = DES3.new(f_read_key,DES3.MODE_EAX,nonce=f_read_nonce)
        plaintext = cipher.decrypt(b64decode(f_read_cipher))
        f_output = open(cipherfile+".dec","w")
        f_output.write(plaintext.decode('utf8'))
        f_output.close()
    except Exception as e: 
        print(str(e))




encrypt("./test.txt")
decrypt("./test.txt.enc","./nonce","./key")
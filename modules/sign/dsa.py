from os import fdopen, read
from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256
from base64 import b64decode
from base64 import b64encode

############## SIGN ##########################

# Sign a message
def dsa_sign(filepath,keypath):
    file_in = open(filepath,"rb")
    sig_file = open(filepath+'.sig','w')
    data = file_in.read()
    hash_obj = SHA256.new(data)
    key_file = open(keypath,"r")
    pv_key = DSA.import_key(key_file.read())
    signer = DSS.new(pv_key, 'fips-186-3')
    sig_file.write(b64encode(signer.sign(hash_obj)).decode('utf8'))
    sig_file.close()
    file_in.close()
    key_file.close()

############## VERIFY ##########################


# Verify the authenticity of the message
def dsa_verify(message_path,keypath,sig_path):
    try:
        f = open(keypath, "r")
        message_file= open(message_path,"rb")
        message = message_file.read()
        hash_obj = SHA256.new(message)
        pub_key = DSA.import_key(f.read())
        verifier = DSS.new(pub_key, 'fips-186-3')
        sig_file = open(sig_path,'rb')
        sig= sig_file.read()
        sig = b64decode(sig)
        verifier.verify(hash_obj,sig)
        print("The message is authentic.")
        f.close()
        sig_file.close
    except ValueError:
        print("The message is not authentic.")


  

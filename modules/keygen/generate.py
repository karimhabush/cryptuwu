from Crypto.PublicKey import RSA
from Crypto.PublicKey import DSA


def generate_rsa_private_key(size):
    key = RSA.generate(size) # 2048 for example
    f = open('./private.pem','wb')
    f.write(key.export_key('PEM'))
    f.close()

def generate_rsa_public_key(private):
    fpr = open(private,'r')
    prkey = RSA.import_key(fpr.read())
    fpb = open('./public.pem','wb')
    pbkey = prkey.publickey().export_key('PEM')
    fpb.write(pbkey)
    fpb.close()
    fpr.close()

# Create a new DSA key
def dsa_keypair(private_path, public_path):
    private_out = open(private_path,"wb")
    public_out = open(public_path,"wb")
    key = DSA.generate(2048)
    private_out.write(key.export_key())
    public_out.write(key.publickey().export_key())
    private_out.close()
    public_out.close()

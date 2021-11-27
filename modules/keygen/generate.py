from Crypto.PublicKey import RSA,DSA


def rsa_keypair(size):
    key = RSA.generate(size) # 2048 for example
    f = open('./rsa_private.pem','wb')
    fpb = open('./rsa_public.pem','wb')
    f.write(key.export_key('PEM'))
    pbkey = key.publickey().export_key('PEM')
    fpb.write(pbkey)
    f.close()
    fpb.close()

# Create a new DSA key
def dsa_keypair(size):
    private_out = open("./dsa_private.pem","wb")
    public_out = open("./dsa_public.pem","wb")
    key = DSA.generate(size)
    private_out.write(key.export_key())
    public_out.write(key.publickey().export_key())
    private_out.close()
    public_out.close()
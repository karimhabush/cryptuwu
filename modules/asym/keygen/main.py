from Crypto.PublicKey import RSA



def generate_private_key(size):
    key = RSA.generate(2048)
    f = open('./private.pem','wb')
    f.write(key.export_key('PEM'))
    f.close()

def generate_public_key(private):
    fpr = open(private,'r')
    prkey = RSA.import_key(fpr.read())
    fpb = open('./public.pem','wb')
    pbkey = prkey.publickey().export_key('PEM')
    fpb.write(pbkey)
    fpb.close()
    fpr.close()


generate_public_key('private.pem')
from Crypto.Hash import SHA224
from Crypto.Hash import MD2
from Crypto.Hash import MD5
from Crypto.Hash import SHA512
from Crypto.Hash import SHA256

def sha224(filepath):
    f_input = open(filepath, 'rb')
    f_read = f_input.read()
    h = SHA224.new()
    h.update(f_read)
    print(h.hexdigest())
    f_input.close()

def sha512(filepath):
    f_input = open(filepath, 'rb')
    f_read = f_input.read()
    h = SHA512.new()
    h.update(f_read)
    print(h.hexdigest())
    f_input.close()

def sha256(filepath):
    f_input = open(filepath, 'rb')
    f_read = f_input.read()
    h = SHA256.new()
    h.update(f_read)
    print(h.hexdigest())
    f_input.close()

def md5(filepath):
    f_input = open(filepath, 'rb')
    f_read = f_input.read()
    h = MD5.new()
    h.update(f_read)
    print(h.hexdigest())
    f_input.close()

def md2(filepath):
    f_input = open(filepath, 'rb')
    f_read = f_input.read()
    h = MD2.new()
    h.update(f_read)
    print(h.hexdigest())
    f_input.close()


md2("./test.txt")
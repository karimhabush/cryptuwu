from Crypto.Hash import SHA224
from Crypto.Hash import MD2
from Crypto.Hash import MD5
from Crypto.Hash import SHA512
from Crypto.Hash import SHA256

def sha224(text):
    h = SHA224.new()
    h.update(text.encode("utf8"))
    print(h.hexdigest())

def sha512(text):
    h = SHA512.new()
    h.update(text.encode("utf8"))
    print(h.hexdigest())

def sha256(text):
    h = SHA256.new()
    h.update(text.encode("utf8"))
    print(h.hexdigest())

def md5(text):
    h = MD5.new()
    h.update(text.encode("utf8"))
    print(h.hexdigest())

def md2(text):
    h = MD2.new()
    h.update(text.encode("utf8"))
    print(h.hexdigest())

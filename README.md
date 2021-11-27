# PKIP
## _A tool for cryptography using pycryptodome_

PKIP is a tool developped using python and pycryptodome used to implement many cryptographic scenarios
## Features

- Random base64/hex string generation 
- RSA and DSA keypair generation
- AES encryption and decryption
- DES3 encryption and decryption
- RSA encryption and decryption
- DSA signatures generation and verification 


## Installation

PKIP requires [Pycryptodome](https://pypi.org/project/pycryptodome/) v3.11+ to run.

```sh
pip install pycryptodome
cd pkip
```
then you can use pkip using the script crypuwu.py
```sh
python3 cryptuwu.py -h
```
## modules and options

PKIP supports the following modules, note that the options in the usage section are mandatory

| option | usage | 
| ------ | ------ | 
| [rand](https://github.com/karimhabush/pkip/blob/main/modules/rand/README.md) | Generates random base64/Hex encoded string of size -s bytes |
| [keygen](https://github.com/karimhabush/pkip/blob/main/modules/keygen/README.md) | Generates an RSA/DSA keypair of size -s bytes |
| [sym](https://github.com/karimhabush/pkip/blob/main/modules/asym/README.md) | refers to symetric encryption, it supports AES and DES encryption/decryption|
| [asym](https://github.com/karimhabush/pkip/blob/main/modules/asym/README.md) | refers to symetric encryption, it supports RSA encryption/decryption |
| [sign](https://github.com/karimhabush/pkip/blob/main/modules/sign/README.md) | create and verify DSA signatures |
| [encoder](https://github.com/karimhabush/pkip/blob/main/modules/encoder/README.md) | base64 encode files |
| [hash](https://github.com/karimhabush/pkip/blob/main/modules/hash/README.md) | hash files, it supports SHA224, SHA512, SHA256, MD2, MD5 |


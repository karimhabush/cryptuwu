#!/usr/bin/env python3.9

import argparse
from modules.asym.rsa import rsa_decrypt, rsa_encrypt
from modules.rand.random import randgen
from modules.hash.hash import sha224, sha256, sha512, md2, md5
from modules.encoder.encode import encode_base64, decode_base64
from modules.sign.dsa import dsa_sign, dsa_verify
from modules.sym import aes, key_aes, des3
from modules.keygen import generate

def main():
    parser = argparse.ArgumentParser(description='add, modify and delete upstream nodes')
    parser.add_argument(
        'mod', choices=['rand', 'sym', 'asym','hash','encode','keygen','sign'], help='Choose a command to execute.')
    parser.add_argument(
        '-H', '--hash', choices=['sha224', 'sha256', 'sha512','md2','md5'], help='select the type of hash')
    parser.add_argument(
        '-t', '--type', choices=['base64', 'hex'], help='select the type of encoding')
    parser.add_argument(
        '--stype', choices=['aes', 'des3'], help='select the type of symetric cryptography algorithm wanted')
    parser.add_argument(
        '--ktype', choices=['rsa', 'dsa'], help='select the type of Keypair you want to generate')
    parser.add_argument(
        '--do', choices=['encrypt', 'decrypt', 'sign', 'verify'], help='select the type of encoding')
    parser.add_argument(
        '-s', '--size', type=int, help='select the size')
    parser.add_argument(
        '-i', '--input', type=str, help='Choose an input file')
    parser.add_argument(
        '-k', '--key', type=str, help='Select the key file path')
    parser.add_argument(
        '-n', '--nonce', type=str, help='Select the nonce file path for the des3 decryption')
    parser.add_argument(
         '--sig', type=str, help='Select the signature file path')

    args = parser.parse_args()

    if args.mod == "rand":
        if args.input is None:
            print("the parameter --input is required!")
        else :
            print(randgen(args.size,args.type))

    elif args.mod == "hash":
        if args.input is None:
            print("the parameter --input is required!")
        elif args.hash == 'sha224':
            sha224(args.input)
        elif args.hash == 'sha256':
            sha256(args.input)
        elif args.hash == 'sha512':
            sha512(args.input)
        elif args.hash == 'md2':
            md2(args.input)
        elif args.hash == 'md5':
            md5(args.input)
    
    elif args.mod == "encode":
        if args.encode is not None : 
            encode_base64(args.input)
        elif args.decode is not None : 
            decode_base64(args.input)

    elif args.mod == "sym":
        if args.input is None:
            print("the parameter --input is required!")
        if args.stype == "aes":
            if args.do is None :
                print("the parameter --do is required!")
            elif args.do == "encrypt" :
                if args.key is None :
                    aes.encrypt(args.input)
                else :
                    key_aes.encrypt(args.input, args.key)
            elif args.do == "decrypt" : 
                if args.key is None : 
                    aes.decrypt(args.input)
                else : 
                    key_aes.decrypt(args.input,args.key)
        if args.stype == "des3":
            if args.do is None :
                print("the parameter --do is required!")
            elif args.do == "encrypt" : 
                des3.encrypt(args.input)
            elif args.do == "decrypt" : 
                if args.key is None : 
                    print("the parameter --key is required!")
                elif args.nonce is None : 
                    print("the parameter --nonce is required!")
                else : 
                    des3.decrypt(args.input,args.nonce, args.key)


    elif args.mod == "asym":
        if args.do is None : 
            print("the parameter --do is required!")
        if args.input is None:
            print("the parameter --input is required!")
        if args.do == "encrypt":
            if args.key is None :
                print("the parameter --key is required, please enter a valid public key path")
            else:
                rsa_encrypt(args.input, args.key)
        elif args.do == "decrypt":
            if args.key is None :
                print("the parameter --key is required, please enter a valid private key path")
            else:
                rsa_decrypt(args.input, args.key)
        

    elif args.mod == "keygen":
        if args.size is None :
            print("the parameter --size is required! [indicates size of the key. example : 2048]")
        elif args.ktype is None :
            print("the parameter --ktype is required! [indicates type of the key. choices : rsa, dsa]")
        elif args.ktype == "rsa":
            generate.rsa_keypair(args.size)
        elif args.ktype == "dsa":
            generate.dsa_keypair(args.size)

    elif args.mod == "sign":
        if args.input is None: 
            print("the parameter --input is required!")
        if args.do is None:
            print("the parameter --do is required! [ sign / Verify ]")
        if args.do == "sign":
            if args.key is None: 
                print("the parameter --key is required! please enter a valid private key path")
            else : 
                dsa_sign(args.input, args.key)
        elif args.do == "verify":
            if args.key is None: 
                print("the parameter --key is required! please enter a valid public key path")
            if args.sig is None: 
                print("the parameter --sig is required! Please enter a valid signature path")
            else : 
                dsa_verify(args.input, args.key, args.sig)
            
if __name__ == "__main__":
    main()
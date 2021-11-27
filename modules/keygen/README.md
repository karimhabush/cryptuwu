# Keypair Generation
 _PKIP module for generating keypairs s_

>It supports RSA and DSA keypair generation

##  Usage

```sh
python3 cryptuwu.py keygen [options]
```

| option |type| descrption|
| -----|-| -----|
| -s / --size | mandatory | specify the private key size |
|--ktype  |mandatory | specify wether to generate RSA or DSA keys (rsa/dsa)

the output will be two files, one for the public ke and one for the private
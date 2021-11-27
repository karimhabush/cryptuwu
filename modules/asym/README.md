# Asymetric encryption
 _PKIP module for assymetric encryption operations_

>It supports RSA encryption and decryption 

##  RSA encryption/decryption

```sh
python3 cryptuwu.py asym [options]
```

| option |type| descrption|
| -----|-| -----|
| --do |mandatory | specify if it is an encryption or decryption [encrypt/decrypt]|
|-i / --input |mandatory | specify an input file|
| -k / --key |mandatory| specify a public key file path for the encryption and a private key file path for decryption |

the output file will be **_input-file-name.enc_**

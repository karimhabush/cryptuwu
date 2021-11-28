# Symetric encryption
 _cryptuwu module for symetric encryption operations_

>It supports AES256/DES3 encryption and decryption 

## Usage

```sh
python3 cryptuwu.py --stype [aes/des3] [options]
```

## AES encryption/decryption

```sh
python3 cryptuwu.py --stype aes [options]
```

| option |type| descrption|
| -----|-| -----|
| --do |mandatory | specify if it is an encryption or decryption [encrypt/decrypt]|
|-i / --input |mandatory | specify an input file|
| -k / --key |optional| specify a secret key file path (if this argument is **None**, a password will be required to generate a key using md5 hash) |

the output file will be **_input-file-name.enc_**


## DES3 encryption/decryption

```sh
python3 cryptuwu.py --stype des3 [options]
```

| option |type| descrption|
| -----|-| -----|
| --do |mandatory| specify if it is an encryption or decryption [encrypt/decrypt]|
|-i / --input |mandatory | specify an input file|
| -k / --key |mandatory| specify a secret key file path |
| -n / --nonce |mandatory in decryption| specify a nonce file path 

the output file will be **_input-file-name.enc_**

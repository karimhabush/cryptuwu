# Signatures
 _cryptuwu module for generating dsa signatures_

>It supports dsa signatures generation and verification

##  Usage

```sh
python3 cryptuwu.py sign [options]
```

| option |type| descrption|
| -----|-| -----|
| -i / --input | mandatory | specify the input filepath |
|--do| mandatory | specify if it's a signature generation or verification operation (sign/verify)|
|-k / --key | mandatory | specify the **private** key for signature generation or the **public** key for signature verification|
|--sig | mandatory for signature verification | specify the signature filepath


# Python RansomWare Manual

## Set Up

`pip3 install cryptography`

## Usage

To encrypt a file, launch : <br>
- `python3 RansomWare.py <file-to-encrypt> -e --encryption-type <symmetric/asymmetric>` <br> 
- `python3 RansomWare.py <file-to-encrypt> --encrypt -t <symmetric/asymmetric>` <br>
Then create a password to encrypt your file. <br>

To decrypt a file, launch : <br>
- `python3 RansomWare.py <file-to-decrypt> --decryption-type <symmetric/asymmetric>` <br>
- `python3 RansomWare.py <file-to-decrypt> -d -t <symmetric/asymmetric>` <br>

Then enter the password you used to encrypt your original file. <br>
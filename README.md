# Python RansomWare Manual

## Set Up

`pip3 install cryptography`

## Usage

To encrypt a file, launch : <br>
- `python3 symmetric.py <file-to-encrypt> -e` <br> 
- `python3 symmetric.py <file-to-encrypt> --encrypt` <br>
Then create a password to encrypt your file. <br>

To decrypt a file, launch : <br>
- `python3 symmetric.py <file-to-decrypt> -d` <br>
- `python3 symmetric.py <file-to-decrypt> --decrypt` <br>

Then enter the password you used to encrypt your original file. <br>
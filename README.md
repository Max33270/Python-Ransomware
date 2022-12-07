# Python RansomWare Manual

## Set Up

`pip3 install cryptography`

## Usage

To encrypt a file, launch : <br>
- `python3 RansomWare.py yourfiletoencrypt.txt --encrypt --salt-size 16` <br> 
- `python3 RansomWare.py yourfiletoencrypt.txt -e --salt-size 16`

Then create a password to encrypt your file. <br>

To decrypt a file, launch : <br>
- `python3 RansomWare.py yourFileToDecrypt.txt --decrypt` <br>
- `python3 RansomWare.py yourFileToDecrypt.txt -d`

Then enter the password you used to encrypt your original file. <br>
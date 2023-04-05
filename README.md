# Python RansomWare Manual

## Prerequisites <br>

`Python 3` <br>
`pip3 install cryptography` <br> <br>

### I. Symmetric Encryption and Decryption <br>

`cd Symmetric` <br>

#### 1. Encrypting a file
Launch one of the following commands and enter a password : <br>
`python3 symmetric_encryption_decryption.py -e <file-to-encrypt>` <br>
`python3 symmetric_encryption_decryption.py --encrypt <file-to-encrypt>` <br>

#### 2. Decrypting a file
Launch one of the following commands and enter the password you used to encrypt your file : <br>
`python3 symmetric_encryption_decryption.py -d <file-to-decrypt>` <br>
`python3 symmetric_encryption_decryption.py --decrypt <file-to-decrypt>` <br> <br>


### II. Asymmetric Encryption and Decryption

`cd Asymmetric` <br>

#### 1. Creating a key pair
Launch the following command : <br>
`python3 create_keys.py` <br>

#### 2. Encrypting a file 
Launch the following command : <br>
`python3 asymmetric_file_encryption.py` <br>

#### 3. Encrypting an input from the terminal
Launch the following command : <br>
`python3 asymmetric_string_encryption.py` <br>
Enter the string you want to encrypt <br>

#### 4. Decrypting a file / an input from the terminal saved in a file :
Launch the following command : <br>
`python3 asymmetric_file_decryption.py` <br> <br>

This project is for educational purposes only. <br>
Have fun and don't use this for malicious purposes !

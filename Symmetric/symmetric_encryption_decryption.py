from cryptography.fernet import Fernet
import cryptography
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
import secrets
import base64
import getpass
import argparse
import os 

# Create the salt.salt file
def create_salt_file():
    with open('salt.salt', 'w') as f:
        f.write("")

# Create the Keys folder
if not os.path.exists("Keys"):
    os.makedirs("Keys")

# Add the generated key with Fernet to key.key
def write_key():
    key = Fernet.generate_key()
    with open("Keys/key.key", "wb") as key_file:
        key_file.write(key)


# Encrypt the cotents of a file with the key
def encrypt_file(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)


# Encrypt the cotents of a folder with the key
def encrypt_folder(folder, key):
    for root, dirs, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)


# Decrypt the contents of a file with the same key
def decrypt_file(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    try:
        decrypted_data = f.decrypt(encrypted_data)
    except cryptography.fernet.InvalidToken:
        print("Incorrect password, sorry")
        return
    with open(filename, "wb") as file:
        file.write(decrypted_data)
    print("File decrypted successfully")


# Decrypt the contents of a file with the same key
def decrypt_folder(folder, key):
    for root, dirs, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            decrypt_file(file_path, key)


# Generate a 16 byte salt to make the password more secure
def generate_salt(size=16):
    return secrets.token_bytes(size)


# Derives a 32 byte key from a password and salt while optimizing computational and memory usage 
def derive_key(salt, password):
    pepper = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1)
    return pepper.derive(password.encode())


# Load the salt from the salt.salt file
def load_salt():
    return open("salt.salt", "rb").read()


# Generates a key from a password and salt
def generate_key(password, salt_size=16, salt_exists=False, create_salt=True):
    if salt_exists:
        salt = load_salt()
    elif create_salt:
        salt = generate_salt(salt_size)
        with open("salt.salt", "wb") as salt_file:
            salt_file.write(salt)
    derived_key = derive_key(salt, password)
    return base64.urlsafe_b64encode(derived_key)


# Main
def main():
    parser = argparse.ArgumentParser(description="Encrypt/Decrypt")
    parser.add_argument("file", help="File to encrypt/decrypt")
    parser.add_argument("-e", "--encrypt", action="store_true",help="If you want to encrypt please enter your file followed by -e or --encrypt.")
    parser.add_argument("-d", "--decrypt", action="store_true", help="If you want to decrypt please enter your file followed by -d or --decrypt .")

    args = parser.parse_args()
    file = args.file

    if args.encrypt:
        password = getpass.getpass("Enter the password for encryption: ")
    elif args.decrypt:
        password = getpass.getpass("Enter the password you used for encryption: ")
        
    key = generate_key(password, salt_exists=True)
    encrypt_ = args.encrypt
    decrypt_ = args.decrypt

    if encrypt_ and decrypt_:
        print("Please specify whether you want to encrypt the file or decrypt it.")
    elif encrypt_:
        if os.path.isfile(file):
            encrypt_file(file, key)
        elif os.path.isdir(file):
            encrypt_folder(file, key)
    elif decrypt_:
        if os.path.isfile(file):
            decrypt_file(file, key)
        elif os.path.isdir(file):
            decrypt_folder(file, key)
    else: 
        print("Please specify whether you want to encrypt the file or decrypt it.")

# Run the main function
if __name__ == "__main__":
    write_key()
    create_salt_file()
    main()
from cryptography.fernet import Fernet
import cryptography
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
import secrets
import base64
import getpass
import argparse
from cryptography.hazmat.primitives import serialization,hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

# Add the generated key with Fernet to key.key
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


# Encrypt the cotents of a file with the key
def encrypt(filename, key,encryption_type):
    if encryption_type=='symmetric':
        f = Fernet(key)
        with open(filename, "rb") as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(filename, "wb") as file:
            file.write(encrypted_data)
    elif encryption_type=='asymmetric':
        with open(filename, "rb") as file:
            data = file.read()
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        public_key = private_key.public_key()
        ciphertext = public_key.encrypt(
            data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        with open(filename, "wb") as file:
            file.write(ciphertext)

# Decrypt the contents of a file with the same key
def decrypt(filename, key,encryption_type):
    if encryption_type=='symmetric':
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
    elif encryption_type=='asymmetric':
        with open(filename, "rb") as file:
            data = file.read()
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        decrypted_data = private_key.decrypt(
            data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        with open(filename, "wb") as file:
            file.write(        decrypted_data)
        print("File decrypted successfully")


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
    parser.add_argument("-s", "--salt-size", help="If this is set, a new salt with the passed size is generated",type=int)
    parser.add_argument("-e", "--encrypt", action="store_true",help="If you want to encrypt please enter your file followed by -e or --encrypt.")
    parser.add_argument("-d", "--decrypt", action="store_true", help="If you want to decrypt please enter your file followed by -d or --decrypt .")
    parser.add_argument("-t", "--encryption-type", help="If this is set, encryption type can be chosen (symmetric or asymmetric)",type=str)

    args = parser.parse_args()
    file = args.file

    if args.encrypt:
        password = getpass.getpass("Enter the password for encryption: ")
    elif args.decrypt:
        password = getpass.getpass("Enter the password you used for encryption: ")

    if args.salt_size:
        key = generate_key(password, salt_size=args.salt_size, create_salt=True)
    else:
        key = generate_key(password, salt_exists=True)

    encrypt_ = args.encrypt
    decrypt_ = args.decrypt
    encryption_type=args.encryption_type
    if encryption_type not in ['symmetric','asymmetric']:
        print("Please choose valid encryption type")
        return

    if encrypt_ and decrypt_:
        print("Please specify whether you want to encrypt the file or decrypt it.")
    elif encrypt_:
        encrypt(file, key,encryption_type)
    elif decrypt_:
        decrypt(file, key,encryption_type)

if __name__ == "__main__":
    main()



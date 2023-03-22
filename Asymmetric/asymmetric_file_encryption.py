from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def main():
    key_file = open('Keys/public_key.pem', 'rb')

    public_key = serialization.load_pem_public_key(
        key_file.read(),
        backend = default_backend()
    )

    with open("file.txt", "rb") as f:
        file = f.read()
            
    encrypted = public_key.encrypt(
        file,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    with open("file.txt", "wb") as f :
        f.write(encrypted)

    print("Sucessfully encrypted file.txt")
 
        

if __name__ == "__main__":
    input = input("Would you like to encrypt file.txt? (y/n):")
    if input == "y" or input == "Y":
        main()
    else : 
        print("Goodbye!")
        exit()
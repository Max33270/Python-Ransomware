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

    text = input("Enter the text to encrypt: ")
    plain_text = bytes(text, "utf-8")

    encrypted = public_key.encrypt(
        plain_text,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    with open("file.txt", "wb") as f:
        f.write(encrypted)

    print("Text sucessfully encrypted and saved to file.txt")
    
if __name__ == "__main__":
    main()
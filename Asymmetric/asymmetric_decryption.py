from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

# Load private key
with open("Keys/private_key.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
    )

# Read encrypted data from file
with open("file.txt", "rb") as f:
    encrypted = f.read()

# Decrypt data
decrypted = private_key.decrypt(
    encrypted,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Write decrypted data to file
with open("file.txt", "wb") as f:
    f.write(decrypted)

print("Text sucessfully decrypted to it's original value and saved to file.txt")
import cryptography
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import os

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

public_key = private_key.public_key()

serial_private = private_key.private_bytes(
    encoding=serialization.Encoding.PEM, 
    format=serialization.PrivateFormat.PKCS8, 
    encryption_algorithm=serialization.NoEncryption()
)

if not os.path.exists("Keys"):
    os.makedirs("Keys")

with open("Keys/private_key.pem", "wb") as f:
    f.write(serial_private)

serial_pub = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

with open("Keys/public_key.pem", "wb") as f:
    f.write(serial_pub)

print("Private and public keys were created successfully!")
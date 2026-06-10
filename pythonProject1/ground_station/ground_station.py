from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.fernet import Fernet
import hashlib

firmware_path = "../firmware/firmware_v1.txt"

with open(
        "../keys/secret.key",
        "rb"
) as file:

    key = file.read()

cipher = Fernet(key)

with open(
        firmware_path,
        "rb"
) as file:

    firmware_data = file.read()

hash_value = hashlib.sha256(
    firmware_data
).hexdigest()

with open(
        "../keys/private_key.pem",
        "rb"
) as key_file:

    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None
    )

signature = private_key.sign(
    firmware_data,
    padding.PSS(
        mgf=padding.MGF1(
            hashes.SHA256()
        ),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

with open(
        "../transmission/signature.bin",
        "wb"
) as sig_file:

    sig_file.write(signature)

with open(
        "../transmission/hash.txt",
        "w"
) as file:

    file.write(hash_value)

encrypted_data = cipher.encrypt(
    firmware_data
)

with open(
        "../transmission/firmware_package.enc",
        "wb"
) as file:

    file.write(encrypted_data)

print("\nGROUND STATION")

print(
    "\nFirmware Encrypted"
)

print(
    "\nSHA256:"
)

print(hash_value)

print(
    "\nEncrypted Package Sent"
)
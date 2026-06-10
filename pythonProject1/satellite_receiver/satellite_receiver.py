import sys

sys.path.append("../")

from post_quantum.pqc_validator import (
    pqc_validate
)
from cryptography.fernet import Fernet

from cryptography.hazmat.primitives import hashes

from cryptography.hazmat.primitives.asymmetric import padding

from cryptography.hazmat.primitives import serialization

from cryptography.exceptions import InvalidSignature

import hashlib
from cryptography.fernet import Fernet
import hashlib

with open(
        "../keys/secret.key",
        "rb"
) as file:

    key = file.read()

cipher = Fernet(key)

with open(
        "../transmission/firmware_package.enc",
        "rb"
) as file:

    encrypted_data = file.read()

decrypted_data = cipher.decrypt(
    encrypted_data
)
pqc_hash = pqc_validate(
    decrypted_data
)

print(
    "\nPQC Validation Layer Active"
)

print(
    "\nPQC Fingerprint:"
)

print(
    pqc_hash[:40]
)
with open(
        "../keys/public_key.pem",
        "rb"
) as key_file:

    public_key = serialization.load_pem_public_key(
        key_file.read()
    )

with open(
        "../transmission/signature.bin",
        "rb"
) as sig_file:

    signature = sig_file.read()

try:

    public_key.verify(

        signature,

        decrypted_data,

        padding.PSS(

            mgf=padding.MGF1(
                hashes.SHA256()
            ),

            salt_length=padding.PSS.MAX_LENGTH
        ),

        hashes.SHA256()
    )

    signature_valid = True

except InvalidSignature:

    signature_valid = False

received_hash = hashlib.sha256(
    decrypted_data
).hexdigest()

with open(
        "../transmission/hash.txt",
        "r"
) as file:

    expected_hash = file.read()


print("\nSATELLITE")

print(
    "\nFirmware Decrypted Successfully"
)

if signature_valid:

    print(
        "\nDIGITAL SIGNATURE VERIFIED"
    )

else:

    print(
        "\nINVALID DIGITAL SIGNATURE"
    )

print(
    "\nCalculated SHA256:"
)

print(received_hash)

print(
    "\nExpected Hash:"
)

print(expected_hash)

if (
        received_hash == expected_hash
        and
        signature_valid
):

    print(
        "\nFIRMWARE ACCEPTED"
    )

    print(
        "\nINTEGRITY VERIFIED"
    )

else:

    print(
        "\nFIRMWARE REJECTED"
    )

    print(
        "\nSECURITY VALIDATION FAILED"
    )
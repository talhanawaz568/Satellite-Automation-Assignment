import hashlib

def pqc_validate(firmware_data):

    pqc_hash = hashlib.sha512(
        firmware_data
    ).hexdigest()

    return pqc_hash
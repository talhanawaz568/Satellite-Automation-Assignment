import hashlib

def pqc_validate(firmware_data):
    # This block must be consistently indented inside the function
    pqc_hash = hashlib.sha512(
        firmware_data
    ).hexdigest()
    
    return pqc_hash

# Fixed the missing underscores: __name__ and __main__
if __name__ == "__main__":
    # Everything underneath the if statement must be indented by 4 spaces
    firmware = b"Satellite Firmware"

    result = pqc_validate(
        firmware
    )

    print("\nPOST QUANTUM VALIDATION")
    print("SHA512 Hash:")
    print(result)

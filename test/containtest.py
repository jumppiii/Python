def rotate_256(plaintext_hex: str, secret_number: int) -> str:
    """Encrypts a string by adding a secret number and taking the remainder (modulo)"""

    # Convert from hex to bytes, e.g. "aabb" -> b"\xaa\xbb"
    plaintext_bytes = bytes.fromhex(plaintext_hex)

    # This is where the encrypted result will go
    output = []

    # Iterate (go through) all the unencrypted numbers in the plaintext
    for unencrypted_number in plaintext_bytes:
        # Uses modulo, or clock arithmetic, to make sure the result is 8 bits and thus fits in a single byte
        encrypted_number = (unencrypted_number + secret_number) % 256
        # Add it to the output list
        output.append(encrypted_number)

    # Convert the list to bytes, so we can easily use the hex() function to convert it to a hex string
    return bytes(output).hex()

def re_rotate_256(plaintext_hex: str, secret_numer: int) -> str:
    unencrypted_number =
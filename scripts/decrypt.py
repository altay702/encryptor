#!/usr/bin/env python3

import base64
import sys
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

KEY_FILE = "mykey.key"

def load_key() -> bytes:
    with open(KEY_FILE, "rb") as f:
        data_b64 = f.read().strip()
    combined = base64.b64decode(data_b64)
    key = combined[16:]  # skip the salt (16 bytes), keep the 32-byte key
    return key

def decrypt_data(encrypted: bytes, key: bytes) -> bytes:
    """
    The first 12 bytes are the nonce, the remainder is ciphertext+tag.
    """
    nonce = encrypted[:12]
    ciphertext = encrypted[12:]
    aesgcm = AESGCM(key)
    plaintext = aesgcm.decrypt(nonce, ciphertext, None)  # no AAD
    return plaintext

def main():
    if len(sys.argv) < 2:
        print("Usage: ./decrypt.py <path_to_encrypted_file>")
        sys.exit(1)

    enc_file = sys.argv[1]

    # Load the key
    key = load_key()

    # Read the encrypted data
    with open(enc_file, "rb") as f:
        encrypted_data = f.read()

    # Decrypt
    try:
        plaintext = decrypt_data(encrypted_data, key)
    except Exception as e:
        print("Error during decryption (wrong key or corrupted data).")
        sys.exit(1)

    # Write to <file>.dec or your naming convention
    out_file = enc_file + ".dec"
    with open(out_file, "wb") as f:
        f.write(plaintext)

    print(f"Decrypted successfully! Output => {out_file}")

if __name__ == "__main__":
    main()

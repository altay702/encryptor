#!/usr/bin/env python3

import base64
import os
import sys
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

KEY_FILE = "mykey.key"

def load_key() -> bytes:
    # Load the base64-encoded salt+key from KEY_FILE
    with open(KEY_FILE, "rb") as f:
        data_b64 = f.read().strip()
    combined = base64.b64decode(data_b64)
    salt = combined[:16]
    key = combined[16:]  # 32 bytes
    return key 

def encrypt_data(plaintext: bytes, key: bytes) -> bytes:
    """
    Encrypt plaintext using AES-256-GCM.
    We generate a random nonce (12 bytes).
    The output is nonce + ciphertext + tag.
    """
    aesgcm = AESGCM(key)
    nonce = os.urandom(12)  # recommended 96-bit nonce for GCM
    ciphertext = aesgcm.encrypt(nonce, plaintext, None)  # no additional authenticated data
    # Return nonce + ciphertext
    return nonce + ciphertext

def main():
    if len(sys.argv) < 2:
        print("Usage: ./encrypt.py <path_to_file>")
        sys.exit(1)

    filepath = sys.argv[1]

    # Load the key
    key = load_key()

    # Read the file content
    with open(filepath, "rb") as f:
        plaintext = f.read()

    # Encrypt
    encrypted = encrypt_data(plaintext, key)

    # Save to new file (e.g. <original>.enc)
    outpath = filepath + ".enc"
    with open(outpath, "wb") as f:
        f.write(encrypted)

    print(f"File encrypted successfully! Output => {outpath}")

if __name__ == "__main__":
    main()

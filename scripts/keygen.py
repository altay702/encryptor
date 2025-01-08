#!/usr/bin/env python3

import os
import argon2
import base64
import getpass

KEY_FILE = "mykey.key"  # This will be created in the same directory run.sh is executed

def generate_key_from_passphrase(passphrase: str, salt: bytes) -> bytes:
    """
    Use Argon2 to derive a 32-byte key (AES-256) from a password and salt.
    """
    ph = argon2.low_level.hash_secret_raw(
        secret=passphrase.encode('utf-8'),
        salt=salt,
        time_cost=3,      # CPU cost
        memory_cost=65536,# 64 MB memory
        parallelism=1,
        hash_len=32,      # 32 bytes => 256 bits
        type=argon2.low_level.Type.ID
    )
    return ph

def main():
    """
    Prompts the user for a passphrase, creates a salt, derives a key,
    and saves salt + key to mykey.key as base64.
    """
    # Ask for passphrase
    passphrase = getpass.getpass("Enter a password to derive the key: ")
    confirm_passphrase = getpass.getpass("Confirm password: ")
    if passphrase != confirm_passphrase:
        print("Passwords do not match. Aborting.")
        return

    # Generate random salt
    salt = os.urandom(16)  # 128-bit salt

    # Derive the key
    key = generate_key_from_passphrase(passphrase, salt)

    # Combine salt + key
    combined = salt + key  # 16 bytes salt + 32 bytes key = 48 bytes total

    # Encode in base64 to store
    combined_b64 = base64.b64encode(combined)

    # Write to file (overwrite if exists)
    with open(KEY_FILE, "wb") as f:
        f.write(combined_b64)

    print(f"Key generated and saved to {KEY_FILE} (salt+key, base64).")

if __name__ == "__main__":
    main()

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os
import base64


# SHA-256 HASH FUNCTION

def hash_input(data):
    digest = hashes.Hash(hashes.SHA256())
    digest.update(data.encode())
    return digest.finalize()


# KEY GENERATION 

def generate_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    return kdf.derive(password.encode())


# ENCRYPTION 

def encrypt(data, key):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv))
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(data.encode()) + encryptor.finalize()
    return iv + ciphertext


# DECRYPTION 

def decrypt(encrypted_data, key):
    iv = encrypted_data[:16]
    ciphertext = encrypted_data[16:]
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv))
    decryptor = cipher.decryptor()
    return decryptor.update(ciphertext) + decryptor.finalize()


# MAIN FLOW

if __name__ == "__main__":
    user_input = input("Enter message: ")

    print("\n--- HASHING ---")
    original_hash = hash_input(user_input)
    print("SHA-256 Hash:", original_hash.hex())

    print("\n--- KEY GENERATION ---")
    salt = os.urandom(16)
    key = generate_key("my_secure_password", salt)

    print("\n--- ENCRYPTION ---")
    encrypted = encrypt(user_input, key)
    print("Encrypted (base64):", base64.b64encode(encrypted).decode())

    print("\n--- DECRYPTION ---")
    decrypted = decrypt(encrypted, key).decode()
    print("Decrypted:", decrypted)

    print("\n--- INTEGRITY CHECK ---")
    new_hash = hash_input(decrypted)

    if original_hash == new_hash:
        print("Integrity VERIFIED ")
    else:
        print("Integrity FAILED ")

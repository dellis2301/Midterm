# Midterm
# Overview

This project is a simple Python application that demonstrates core cryptographic principles, including confidentiality, integrity, and secure key generation. The program accepts user input, hashes it using SHA-256, encrypts it using AES symmetric encryption, decrypts it, and verifies that the data has not been altered.

# Features
Accepts user input 
Generates SHA-256 hash for integrity checking
Uses PBKDF2HMAC for secure AES key generation
Encrypts data using AES 
Decrypts encrypted data
Verifies integrity by comparing hashes

# How It Works
1. User Input

The program prompts the user to enter a message.

2. Hashing (Integrity)

The input is hashed using SHA-256. This hash is stored and later used to verify that the data has not been changed.

3. Key Generation

A secure AES key is generated using PBKDF2HMAC with:

SHA-256 as the hashing algorithm
A randomly generated salt
100,000 iterations
4. Encryption (Confidentiality)

The message is encrypted using:

AES encryption algorithm
CFB mode
A randomly generated initialization vector 
5. Decryption

The encrypted data is decrypted using the same AES key and IV.

6. Integrity Check

A new SHA-256 hash is generated from the decrypted message and compared to the original hash.
If both match, the integrity of the data is verified.

# Security Concepts
Confidentiality

AES encryption ensures that only someone with the correct key can read the message. Without the key, the encrypted data cannot be understood.

Integrity

SHA-256 hashing ensures that any change to the original message will result in a different hash value, allowing tampering to be detected.

Availability

The system is lightweight and ensures that authorized users can reliably encrypt and decrypt data when needed.

# Role of Entropy and Key Generation Entropy

Entropy refers to randomness used in cryptographic systems. This project uses os.urandom() to generate:

Salt for key derivation
Initialization Vector for encryption

This randomness ensures that encryption results are unpredictable and secure.

# Key Generation

The AES key is derived using PBKDF2HMAC, which strengthens a password by:

Using SHA-256
Adding a random salt
Running 100,000 iterations

This makes brute-force attacks significantly more difficult.

# How to Run
1. Clone or Download the Project

Make sure you have the app.py file in a folder on your computer.

2. Open a Terminal in the Project Folder

Navigate to the folder containing app.py.

3. Install Dependencies

Run the following command:

pip install cryptography
4. Run the Program

Execute the script using:

python app.py

# PB-TIED : *(Password-Based Text & Image Encryption Decryption System)*
PB-TIED is a terminal-based Python application designed for secure encryption and decryption of text and image files using password-based symmetric encryption. It leverages cryptographic standards to provide a secure, user-friendly interface for data protection.

**************************************

## Key Features
* Text Encryption & Decryption
    * Supports both direct string input and .txt files.
    * Uses password-based encryption to secure sensitive textual data.
    * Option to save the encrypted or decrypted text to a user-defined file.

* Image Encryption & Decryption
    * Accepts any image file format (e.g., .jpg, .png, .bmp, etc.).
    * Converts image data to byte streams and encrypts/decrypts them securely.
    * Outputs the result to a new image file, fully restorable to the original.

* Password-Based Key Derivation
    * Users provide a password which is hashed using SHA-256 and encoded to form a secure Fernet key.
    * Ensures that encryption keys are never hardcoded or stored in plaintext.

* Interactive Command-Line Interface
    * Menu-driven interface for ease of use.
    * Error handling for invalid inputs and missing files.
    * Clear prompts and output messages for a seamless experience.

**************************************

## Algorithms and Libraries Used

1. **SHA256** :

SHA-256 is a cryptographic hash function that belongs to the SHA-2 family (developed by the NSA and published by NIST). It generates a fixed-length 256-bit (32-byte) hash value from any input data, regardless of the original size. SHA-256 is considered secure against known cryptographic attacks. It has not been broken and is widely used in government and industry-grade applications.

2. Fernet

Fernet is a symmetric encryption method included in the Python cryptography package. It ensures that a message encrypted with a key can only be decrypted with the same key, and it also provides message integrity through authentication. It combines AES (Advanced Encryption Standard) and HMAC (Hash-based Message Authentication Code) for secure and authenticated encryption. 


**************************************

## Libraries Used
   * **cryptography.fernet** : Encryption and decryption.
   * **hashlib** : SHA-256 hash function.
   * **base64** : Encoding binary data.
   * **os** : File and path checking.
   * **art** : ASCII banner generator for UI.

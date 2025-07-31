# PB-FED : *(Password-Based File Encryption-Decryption Tool)*

PB-FED is a Python-based GUI application designed for the secure encryption and decryption of **text, image, and binary files** using password-derived cryptographic keys. It provides a **user-friendly graphical interface using Tkinter**, making it accessible to both technical and non-technical users for protecting sensitive data.

---

## 🔐 Key Features

### 📄 Text Encryption & Decryption

* Supports direct text input and `.txt` file selection.
* Encrypts and decrypts using password-derived keys.
* Allows saving the output to a user-defined file.

### 🖼️ Image Encryption & Decryption

* Works with common image formats (`.jpg`, `.png`, `.bmp`, etc.).
* Converts image data to byte streams for secure encryption/decryption.
* Produces a new encrypted image file that can be fully restored.

### 📁 Generic File Encryption & Decryption

* Accepts **any file type** (e.g., `.pdf`, `.docx`, `.zip`, `.exe`, etc.).
* Reads and encrypts/decrypts raw binary data.
* Maintains data integrity with password-based symmetric encryption.

### 🔑 Password-Based Key Derivation

* User provides a password which is:

  * Hashed using **SHA-256**
  * Encoded into a **Fernet-compatible key**
* No hardcoded or stored encryption keys—**fully password-based**.

### 🖥️ GUI-based Interface (Tkinter)

* Intuitive interface with buttons, file browsers, and status labels.
* Replaces terminal-based interaction with easy-to-navigate forms.
* Built-in error handling for invalid input, missing files, and wrong passwords.

---

## ⚙️ Algorithms and Cryptographic Principles

### 1. **SHA-256**

* Secure hashing algorithm from the SHA-2 family.
* Produces a 256-bit hash from any input.
* Used to derive a strong encryption key from the user’s password.

### 2. **Fernet (from `cryptography`)**

* Implements AES in CBC mode with a HMAC for authentication.
* Guarantees that encrypted data cannot be tampered with.
* Ensures symmetric encryption and integrity checking.

---

## 📚 Libraries Used

* **`cryptography.fernet`** : For AES-based symmetric encryption and HMAC-based integrity.
* **`hashlib`** : For hashing passwords with SHA-256.
* **`base64`** : For encoding the hashed password into a Fernet-compatible format.
* **`os`** : For file handling and path validation.
* **`tkinter`** : For building the graphical user interface (GUI).
* **`filedialog` & `messagebox` (from tkinter)** : For interactive file selection and alert messages.
* **`art`** *(optional)* : For ASCII banner generation (if reused in GUI splash).

## Liscense 

Liscense under MIT License, Which is a short and permissive open-source license that allows anyone to use, modify, distribute, or even sell the software, as long as the original license and copyright notice are included. It imposes minimal restrictions and is widely used in both open-source and commercial projects. However, it provides no warranty, meaning the author is not liable for any damages caused by the software. Its simplicity and flexibility make it one of the most popular licenses in the software development community.

from cryptography.fernet import Fernet
import os

KEY_FILE = "secret.key"


def load_key():
    """Load the encryption key from the file."""

    with open(KEY_FILE, "rb") as file:
        return file.read()


def generate_key():
    """Generate and save a new encryption key."""

    key = Fernet.generate_key()

    with open(KEY_FILE, "wb") as file:
        file.write(key)

    return key


# Create the key only if it does not already exist
if not os.path.exists(KEY_FILE):
    generate_key()


cipher = Fernet(load_key())


def encrypt_password(password):
    """Encrypt a password."""

    encrypted_password = cipher.encrypt(password.encode())

    return encrypted_password.decode()


def decrypt_password(encrypted_password):
    """Decrypt a password."""

    decrypted_password = cipher.decrypt(encrypted_password.encode())

    return decrypted_password.decode()
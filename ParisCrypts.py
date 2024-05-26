from cryptography.fernet import Fernet as Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from base64 import urlsafe_b64encode
import os
import hashlib

class StringEncryptor:
    def __init__(self, password, salt=None):
        """Initializes the StringEncryptor with a password and optional salt."""
        self.password = password.encode()
        if salt is None:
            salt = os.urandom(16)
        self.salt = salt
        self.key = self._derive_key(self.password, self.salt)
        self.fernet = Fernet(self.key)

    def _derive_key(self, password, salt):
        """Derives a key from the password and salt."""
        kdf = PBKDF2HMAC(
            algorithm=hashlib.sha256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        return urlsafe_b64encode(kdf.derive(password))

    def encrypt(self, plain_text):
        """Encrypts a string and returns the ciphertext in bytes."""
        return self.fernet.encrypt(plain_text.encode())

    def decrypt(self, cipher_text):
        """Decrypts a ciphertext and returns the plaintext in string format."""
        return self.fernet.decrypt(cipher_text).decode()

    def get_salt(self):
        """Returns the salt used for key derivation."""
        return self.salt
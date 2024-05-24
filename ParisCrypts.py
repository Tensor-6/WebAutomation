from cryptography.fernet import Fernet as Fernet

class StringEncryptor:
    def __init__(self, key=None):
        if key is None:
            key = Fernet.generate_key()
        self.key = key
        self.fernet = Fernet(self.key)

    def encrypt(self, plain_text):
        """Encrypts a string and returns the ciphertext in bytes."""
        return self.fernet.encrypt(plain_text.encode())

    def decrypt(self, cipher_text):
        """Decrypts a ciphertext and returns the plaintext in string format."""
        return self.fernet.decrypt(cipher_text).decode()

    def get_key(self):
        """Returns the key used for encryption and decryption."""
        return self.key
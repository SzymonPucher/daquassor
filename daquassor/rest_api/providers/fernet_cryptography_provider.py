from cryptography.fernet import Fernet


class FernetCryptographyProvider:
    def __init__(self, secret_key: str):
        self.encryption_engine = Fernet(secret_key)

    def encrypt(self, string: str):
        return self.encryption_engine.encrypt(string.encode()).decode()

    def decrypt(self, string: str):
        return self.encryption_engine.decrypt(string.encode()).decode()

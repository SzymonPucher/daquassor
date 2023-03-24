from common.config import Config


class ConfigProvider:
    def __init__(self, config=None):
        self.config = config or Config()

    def get_db_connection_url(self):
        return self.config.db_connection_url

    def get_jwt_secret(self):
        return self.config.jwt_secret

    def get_jwt_algorithm(self):
        return self.config.jwt_algorithm

    def get_encryption_key(self):
        return self.config.encryption_key

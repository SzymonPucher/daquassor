from common.config.config import Config


class ConfigProvider:
    def __init__(self, config=None):
        self.config = config or Config()

    def get_db_connection_url(self):
        return self.config.db_connection_url

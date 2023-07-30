class ConfigProvider:
    def __init__(self, config=None):
        self.config = config

    def get_db_connection_url(self):
        return self.config.db_connection_url

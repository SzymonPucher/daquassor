from sqlmodel import SQLModel, create_engine

from common.config_provider import ConfigProvider


def initialize_database():
    config_provider = ConfigProvider()
    SQLModel.metadata.create_all(create_engine(config_provider.get_db_connection_url()))

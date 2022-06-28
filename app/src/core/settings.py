from pydantic import BaseSettings

class Settings(BaseSettings):
  app_name: str = "sinpe"
  couchdb_name: str
  couchdb_password: str
  couchdb_host: str
  couchdb_database: str

  class Config:
    env_file = ".env"

from pydantic import BaseSettings

class Settings(BaseSettings):
  DEBUG: bool = False
  ENV: str = 'dev'

  PROJECT_NAME: str = 'machanic-service'
  PROJECT_API_VERSION: str = '0.1.0'
  DOCS_URL: str = None
  REDOC_URL: str = None

  # OTROS
  TIME_ZONE: str = 'America/Lima'


  class Config:
    env_file = '.env'

Config = Settings()

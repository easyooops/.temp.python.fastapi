from pydantic import BaseSettings

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SQLALCHEMY_DATABASE_URL: str
    
    class Config:
        env_file = ".env"

settings = Settings()
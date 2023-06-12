from pydantic import BaseSettings

class Settings(BaseSettings):
    database_port: str
    database_name: str
    database_hostname: str
    database_username: str
    database_password: str
    secret_key: str
    algorithm: str
    access_token_expiration_in_minutes: int

    class Config:
        env_file = ".env"


settings = Settings()
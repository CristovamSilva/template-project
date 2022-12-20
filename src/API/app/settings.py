from pydantic import BaseSettings


class Settings(BaseSettings):
    host: str = "0.0.0.0" # nosec
    port: int = 8000 # nosec

    class Config:
        env_file = ".env"


settings = Settings()

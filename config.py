from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Contract Serializer"

    class Config:
        env_file = ".env"
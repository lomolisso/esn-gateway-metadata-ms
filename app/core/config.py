import os
from dotenv import load_dotenv

# Retrieve enviroment variables from .env file
#load_dotenv()

SECRET_KEY: str = os.environ.get("SECRET_KEY", "secret_key")
METADATA_MICROSERVICE_HOST: str = os.environ.get("METADATA_MICROSERVICE_HOST", "127.0.0.1")
METADATA_MICROSERVICE_PORT: int = int(os.environ.get("METADATA_MICROSERVICE_PORT", 8007))

TIMEZONE: str = os.environ.get("TIMEZONE", "Chile/Continental")

ORIGINS: list = [
    "*"
]

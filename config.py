import os

POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "secret")
POSTGRES_USER = os.getenv("POSTGRES_USER", "user")
POSTGRES_DB = os.getenv("POSTGRES_DB", "avito_db")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "127.0.0.1")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")
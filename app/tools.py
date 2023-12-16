from schema import SCHEMA_CLASS
from pydantic import ValidationError
from errors import HttpError
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from config import TYPE_DB, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_PORT, POSTGRES_DB

PG_DSN = f"{TYPE_DB}://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
engine = create_engine(PG_DSN)
Session = sessionmaker(bind=engine)

def validate(schema_cls: SCHEMA_CLASS, json_data: dict | list):
    try:
        return schema_cls(**json_data).dict(exclude_unset=True)
    except ValidationError as er:
        error = er.errors()[0]
        error.pop("ctx", None)
        raise HttpError(400, error)

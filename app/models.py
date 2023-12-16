import datetime
import sqlalchemy as sq
from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase



class Base(DeclarativeBase):
    pass


class Adverts(Base):
    __tablename__ = 'adverts'

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=50), unique=True, index=True, nullable=False)
    description = sq.Column(sq.String(length=50), nullable=False)
    time_create = sq.Column(sq.DateTime, server_default=func.now())

    @property
    def dict(self):
        return {'id': self.id,
                'title': self.title,
                'description': self.description,
                'time_create': self.time_create}

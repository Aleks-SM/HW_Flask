import sqlalchemy as sq
from app import app


if __name__ == '__main__':
    app.run(debug=True)
    engine = sq.engine.create_engine()
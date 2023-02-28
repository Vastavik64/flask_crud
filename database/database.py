from sqlalchemy import create_engine
# from sqlalchemy. import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base


SQLALCHEMY_DATABASE_URI = "postgresql://postgres:vastavik@localhost:5432/vasu_database"

engine = create_engine(
    SQLALCHEMY_DATABASE_URI
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_USER = "postgres"
DATABASE_PASSWORD = "postgres"
DATABASE_URL = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@localhost/escola"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

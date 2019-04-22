from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine("sqlite:///oo_sqlalchemy.db")
session = scoped_session(sessionmaker(engine))
Base = declarative_base()

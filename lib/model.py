# imports
from sqlalchemy import create_engine, Integer, Column, String, ForeignKey, desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Connection string and Database setup
conn = 'sqlite:///wharehouse.db'

engine = create_engine(conn)

Base = declarative_base()

# Session
Session = sessionmaker(bind=engine)

session = Session()


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


# Category Model

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer(),primary_key=True)
    category_name = Column(String(150),nullable=False)

    #relationship
    products = relationship("Product",backref="category")
    
# Employee Model
class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer(),primary_key=True)
    employee_firstname = Column(String(50),nullable=False)
    employee_lastname = Column(String(50),nullable=False)
    employee_email = Column(String(50),nullable=False)

    # relationship
    products = relationship("Product",backref="employee")


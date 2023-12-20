# imports
from sqlalchemy import create_engine, Integer, Column, String, ForeignKey
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

    def __repr__(self):
        return f"Category id: {self.id} Category name: {self.category_name}"
    
# Employee Model
class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer(),primary_key=True)
    employee_firstname = Column(String(50),nullable=False)
    employee_lastname = Column(String(50),nullable=False)
    employee_email = Column(String(50),nullable=False)

    # relationship
    products = relationship("Product",backref="employee")

    def __repr__(self):
        return f"Employee id: {self.id}, FirstName: {self.employee_firstname}, LastName: {self.employee_lastname}"

# Product Model
class Product(Base):
    __tablename__ = "products"
    id = Column(Integer(),primary_key=True)
    product_name = Column(String(50),nullable=False)
    product_size = Column(Integer(),nullable=False)
    product_quantity = Column(Integer(),nullable=False)
    product_category = Column(Integer,ForeignKey('categories.id'))
    added_by = Column(Integer(),ForeignKey('employees.id'))

    def __repr__(self):
        return f" Product id: {self.id}, Product name: {self.product_name}, Product size: {self.product_size}, Product quantity: {self.product_quantity}"

Base.metadata.create_all(engine)

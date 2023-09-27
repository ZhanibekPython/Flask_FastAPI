import databases
from pydantic import BaseModel, Field
from sqlalchemy import MetaData, create_engine, Table, Boolean, String, Integer, Column, Text, Float, ForeignKey

DATABASE_URL = "sqlite:///sem#6_HW.db"
database = databases.Database(DATABASE_URL)
metadata = MetaData()

user = Table('user', metadata,
             Column('id', Integer, primary_key=True),
             Column('name', String(30), nullable=False),
             Column('surname', String(30), nullable=False),
             Column('email', String(50), unique=True),
             Column('psw', String(30), nullable=False),
             )


class User(BaseModel):
    id: int
    name: str = Field(..., title='Name', max_length=30)
    surname: str = Field(..., title='Surname', max_length=30)
    email: str = Field(None, title='Email', max_length=50)
    psw: str = Field(..., title='Password', max_length=50)


class UserIn(BaseModel):
    name: str = Field(..., title='Name', max_length=30)
    surname: str = Field(..., title='Surname', max_length=30)
    email: str = Field(None, title='Email', max_length=50)
    psw: str = Field(..., title='Password', max_length=50)


product = Table('product', metadata,
                Column('id', Integer, primary_key=True),
                Column('name', String(30), nullable=False),
                Column('description', Text, nullable=False),
                Column('price', Float),
                )


class Product(BaseModel):
    id: int
    name: str = Field(..., title='Name', max_length=30)
    description: str = Field(None, title='Description')
    price: float = Field(..., title='Price', max_length=50)


class ProductIn(BaseModel):
    name: str = Field(..., title='Name', max_length=30)
    description: str = Field(None, title='Description')
    price: float = Field(..., title='Price', max_length=50)


order = Table('order', metadata,
              Column('id', Integer, primary_key=True),
              Column('user_id', Integer, ForeignKey('user.id')),
              Column('product_id', Integer, ForeignKey('order.id')),
              Column('order_date', String, nullable=False),
              Column('status', Boolean, nullable=False),
              )


class Order(BaseModel):
    id: int
    order_date: str = Field(..., title='Date of order', pattern='\d\d/\d\d/\d{4}')
    status: bool = Field(None, title='Order status')


class OrderIn(BaseModel):
    order_date: str = Field(..., title='Date of order', pattern='\d\d/\d\d/\d{4}')
    status: bool = Field(None, title='Order status')


if __name__ == '__main__':
    engine = create_engine(DATABASE_URL)
    metadata.create_all(engine)
from typing import List

import databases
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from sqlalchemy import MetaData, Table, Boolean, String, Integer, Column, Text, Float, ForeignKey
from sqlalchemy import create_engine

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


hw = FastAPI()


@hw.get('/', response_class=HTMLResponse)
async def index():
    return '<h1> Ну, здравствуй! Проходи, чувствуй себя как дома </h1>'


@hw.get('/users/', response_model=List[User])
async def get_users(usr: User):
    query = user.select()
    return await database.fetch_all(query)


@hw.get('/users/{user_id}', response_model=User)
async def get_one_user(user_id: int, usr: User):
    query = usr.select().where(usr.c.id == user_id)
    return await database.fetch_one(query)


@hw.post('/users/', response_model=UserIn)
async def add_new_user(usr: UserIn):
    query = usr.insert().values(name=usr.name, surname=usr.surname, email=usr.email, psw=usr.psw)
    res = await database.execute(query)
    return res


@hw.put('/users/{user_id}', response_model=User)
async def change_user(user_id: int, new_user: User):
    query = user.update().where(user.c.id == user_id).values(**new_user.dict())
    await database.execute(query)


@hw.delete('/users/{user_id}')
async def delete_user(user_id: int):
    query = user.delete().where(user.c.id == user_id)
    await database.execute(query)
    return {'message': 'User was deleted'}


@hw.get('/products/', response_model=List[Product])
async def get_products(prodct: Product):
    query = prodct.select()
    return await database.fetch_all(query)


@hw.get('/products/{product_id}', response_model=Product)
async def get_one_product(product_id: int, prodct: Product):
    query = prodct.select().where(prodct.c.id == product_id)
    return await database.fetch_one(query)


@hw.post('/products/', response_model=ProductIn)
async def add_new_product(prodct: ProductIn):
    query = prodct.insert().values(name=prodct.name, description=prodct.description, price=prodct.price)
    res = await database.execute(query)
    return res


@hw.put('/products/{product_id}', response_model=Product)
async def change_product(product_id: int, new_product: Product):
    query = product.update().where(product.c.id == product_id).values(name=product.name,
                                                                      description=product.description,
                                                                      price=product.price)
    await database.execute(query)


@hw.delete('/products/{product_id}')
async def delete_product(product_id: int):
    query = product.delete().where(product.c.id == product_id)
    await database.execute(query)
    return {'message': 'Product was deleted'}


@hw.get('/orders/', response_model=List[Order])
async def get_orders(ordr: Order):
    query = ordr.select()
    return await database.fetch_all(query)


@hw.get('/orders/{order_id}', response_model=Order)
async def get_one_order(order_id: int, ordr: Order):
    query = ordr.select().where(ordr.c.id == order_id)
    return await database.fetch_one(query)


@hw.post('/orders/', response_model=OrderIn)
async def add_new_order(ordr: OrderIn):
    query = order.insert().values(order_date=ordr.order_date, status=ordr.status)
    res = await database.execute(query)
    return res


@hw.put('/orders/{order_id}', response_model=Order)
async def change_order(uorder_id: int, new_order: Order):
    query = order.update().where(order.c.id == order_id).values(**new_order.dict())
    await database.execute(query)


@hw.delete('/orders/{order_id}')
async def delete_order(order_id: int):
    query = order.delete().where(order.c.id == order_id)
    await database.execute(query)
    return {'message': 'User was deleted'}


engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)

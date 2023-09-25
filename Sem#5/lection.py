from fastapi import FastAPI
import logging
from typing import Optional
from pydantic import BaseModel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Hello world!'}


@app.get('/items/{item_id}')
async def read_item(item_id: int, q: str = None):
    return {'item_id': item_id, 'q': q}


@app.get('/logging-check')
async def logging_check():
    logger.info('Отработал GET запрос')
    return {"Hello": "Johny"}


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.post('/items/')
async def create_item(item: Item):
    logger.info('Обработал POST запрос')
    return item


@app.put('/items/{item_id}')
async def update_item(item_id: int, item: Item):
    logger.info(f'Обработал PUT запрос для item_id = {item_id}.')
    return {'item_id': item_id, 'item': item}


@app.delete('/items/{item_id}')
async def delete_item(item_id: int):
    logger.info(f'Обработал DELETE запрос для item_id = {item_id}.')
    return {'item_id': item_id}

# Необходимо создать API для управления списком задач. Каждая задача
# должна содержать заголовок и описание. Для каждой задачи должна быть
# возможность указать статус (выполнена/не выполнена).
# API должен содержать следующие конечные точки:
# — GET /tasks — возвращает список всех задач.
# — GET /tasks/{id} — возвращает задачу с указанным идентификатором.
# — POST /tasks — добавляет новую задачу.
# — PUT /tasks/{id} — обновляет задачу с указанным идентификатором.
# — DELETE /tasks/{id} — удаляет задачу с указанным идентификатором.
# Для каждой конечной точки необходимо проводить валидацию данных
# запроса и ответа. Для этого использовать библиотеку Pydantic.

import logging

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel

# from sqlalchemy import create_engine, Column, Integer, String, Text, Boolean
# from sqlalchemy.orm import as_declarative

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title='Sem#5_HW')

# engine = create_engine(url='mysql:///homework.db')
#
# @as_declarative()
# class TaskModel:
#     __tablename__ = 'Task'
#     id = Column(Integer, autoincrement=True, primary_key=True)
#     title = Column(String(30), nullable=False)
#     description = Column(Text)
#     status = Optional[Boolean]

fake_db = [
    {'id': 1, 'title': 'Birthday', 'description': 'Buy a present', 'status': True},
    {'id': 2, 'title': 'Balcony', 'description': 'Finish repair works at the balcony', 'status': False},
    {'id': 3, 'title': 'Cleaning', 'description': 'Order cleaning service', 'status': True},
    {'id': 4, 'title': 'Buyout', 'description': 'Purchase goods for work', 'status': False},
    {'id': 5, 'title': 'Fishing', 'description': 'Renew fishing lures for the next season', 'status': False}
]


class Task(BaseModel):
    title: str
    description: str
    status: bool


@app.get('/', response_class=HTMLResponse)
async def main_page():
    logger.info('Main page')
    return '<h1> Welcome to our main page </h1>'


@app.get('/tasks', response_class=JSONResponse)
async def tasks():
    logger.info('Tasks displayed')
    return JSONResponse(content=fake_db, status_code=200)


@app.post('/tasks/')
async def add_task(task: Task):
    logger.info('Added new task')
    return task


@app.put('/tasks/{id}')
async def correct_task(id: int, task: Task):
    logger.info(f'Task {id} was refreshed')
    return task


@app.delete('/tasks/{id}')
async def delete_task(id: int, task: Task):
    logger.info(f'Task {id} was deleted')
    return task

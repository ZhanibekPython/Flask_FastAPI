import sqlalchemy as db
from sqlalchemy import Table, TIMESTAMP
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
from datetime import datetime


engine = db.create_engine('sqlite:///task1.db')
connection = engine.connect()
metadata = db.MetaData()

class Task(BaseModel):
    id: int
    title: str
    description: str
    status: str

tasks = Table('tasks', metadata,
              db.Column('task_id', db.Integer, primary_key=True),
              db.Column('task_description', db.Text, nullable=False),
              db.Column('task_date', TIMESTAMP, default=datetime.utcnow),
              db.Column('status', db.String))

metadata.create_all(engine)


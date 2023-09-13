from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
    __tablename__ = 'Students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    surname = db.Column(db.String(60), nullable=False)
    age = db.Column(db.Integer, default=18)
    gender = db.Column(db.Enum('male', 'female'), nullable=False)
    group = db.Column(db.Enum('math', 'physics'))
    email = db.Column(db.String(50))
    departments = db.relationship('Department', backref='student', lazy=True)


class Department(db.Model):
    __tablename__ = 'Departments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    students = db.Column(db.Integer, db.ForeignKey('student.id'))

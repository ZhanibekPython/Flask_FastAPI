from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from models import db, Student, Department

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db = SQLAlchemy(app)


@app.route('/')
def index():
    db.create_all()
    return render_template('index.html', title='Добро пожаловать!')

@app.route("/register/", methods=['GET', 'POST'])
def register():
    if request.method == 'post':
        name = request.form.get('name')
        surname = request.form.get('surname')
        age = request.form.get('age')
        gender = request.form.get('gender')
        group = request.form.get('group')
        dep_id = request.form.get('dep_id')
    student = Student(name=name, surname=surname, age=age, gender=gender, group=group, dep_id=dep_id)
    db.session.add(student)
    db.session.commit()


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task2.db'
db = SQLAlchemy(app)


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer)
    copies = db.Column(db.Integer)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    author = db.relationship('Author', backref='books')

db.create_all()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'post':
        



if __name__ == '__main__':
    app.run(debug=True)

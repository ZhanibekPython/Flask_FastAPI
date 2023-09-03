from flask import Flask, render_template

# ch = '''Проверка будет ли выходить ссылка: <a href="#">Сcылка</a>'''
# check = escape(ch)
# print(check)

app = Flask(__name__)

collection = ['Один', 'Два', 'Три']


@app.route('/')
def main():
    return render_template('about.html', title="Главная страница")



if __name__ == '__main__':
    app.run()

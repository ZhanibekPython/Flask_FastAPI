from flask import Flask, escape, url_for

app = Flask('app')


@app.route('/')
def index():
    return 'Введи путь к файлу в адресной строке'


@app.route('/<path:file>/')
def get_file(file):
    print(file)
    # return f'Ваш файл находится в: {file}'
    return f'Ваш файл находится в: {escape(file)}'


@app.route('/test_url_for/<int:num>/')
def test_url(num):
    text = f'В num лежит {num}<br>'
    text += f'Функция {url_for("test_url", num=42) = }<br>'
    text += f'Функция {url_for("test_url", num=42, data="new_data") = }<br>'
    text += f'Функция {url_for("test_url", num=42, data="new_data", pi=3.14151) = }<br>'
    return text


if __name__ == '__main__':
    app.run()

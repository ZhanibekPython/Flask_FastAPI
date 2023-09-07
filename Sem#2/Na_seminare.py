from flask import Flask, render_template, url_for, redirect, request, flash
from werkzeug.utils import secure_filename
from pathlib import Path, PurePath

app = Flask(__name__)
app.secret_key = b'29084c5e2c70ea67cff3e65acc0394c687a3144c39537a08307d59bbb938f46a'


@app.route('/')
def main_page():
    return render_template('base.html')


@app.route('/greet/', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        name = request.form['name']
        return redirect(url_for('welcome', name=name))


@app.route('/welcome/<name>')
def welcome(name):
    return f'Ну здравствуй, {name}'


@app.route('/task2/')
def task2():
    return render_template('task2.html')


@app.route('/task2/upload/')
def task2_upload():
    if request.method == 'POST':
        image = request.files.get('image')
        filename = secure_filename(image.filename)
        Path(Path.cwd(), 'Sem#2', 'static', 'uploads').mkdir(exist_ok=True)
        image.save(PurePath.joinpath(Path.cwd(), 'static', 'uploads', filename))
        return flash('Ваш файл был загружен')
    return render_template('task2upload.html')


@app.route('/task3/', methods=['GET', 'POST'])
def task3():
    db = {'Sasha': 111, 'Masha': 222, 'Dasha': 333, 'Kasha': 444, 'Innokentii': 555}
    chel = request.form.get('login')
    pasw = request.form.get('password')
    if chel in db.keys() and pasw == db['chel']:
        return redirect(url_for('welcome', name=chel))
    else:
        flash('Wrong login or password!', 'danger')


@app.route('/task6', methods=['GET', 'POST'])
def task6():
    if request.method == 'post':
        name = request.form.get('name')
        age = int(request.form.get('age'))
        if name.isalpha() and 0 <= age <= 120:
            return redirect(url_for('task2', name=name))
        else:
            return render_template('404.html')
    return render_template('task6.html')


# @app.get('/task7')
# def task7_get():
#     return render_template('task7.html')
#
#
# @app.post('/task7')
# def task7_post():
#     num = int(request.form.get('num'))
#     return f'{num} = {num ** 2}'
@app.route('/task7', methods=['get', 'post'])
def task7():
    if request.method == 'post':
        num = int(request.form.get("num"))
        return url_for('task7/res', res=num)
    return render_template('task7.html')


@app.route('/task7/res/<int:num>')
def task7_res(num):
    return f'{num} = {num ** 2}'


@app.route('/task8/', methods=['GET', 'POST'])
def task8():
    if request.method == 'POST':
        if not request.form.get('name'):
            flash('Ошибка, введите имя!', 'danger')
            return render_template('404.html'), 404
        name = request.form.get('name')
        flash('Сообщение отправлено', 'success')
        return f'Привет, {name}'
    render_template('task8.html')


if __name__ == '__main__':
    app.run()

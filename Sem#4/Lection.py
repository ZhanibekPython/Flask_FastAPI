from flask import Flask, render_template, flash, request, redirect, session, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = b'jnndinwdivnowidnvo2dnvoi2nd0iv2n2nv'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'post':
        if len(request.form['name']) < 3:
            flash('В имени должно быть более 2 символов!', category='error')
        else:
            flash('Все хорошо!', category='success')
    return render_template('register.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if 'userLogged' in  session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'post' and request.form['username'] == 'johny' and request.form['psw'] == '123':
        session['userLogged'] = request.form['userLogged']
        return redirect(url_for('profile', username=session['userLogged']))

    return render_template('login.html', title='Авторизация')


@app.route('/profile/<username>')
def profile(username):
    return f'Профиль пользователя: {username}'


@app.errorhandler(404)
def pageNotFound(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)

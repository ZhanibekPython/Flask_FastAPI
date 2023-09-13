from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        resp = make_response(redirect(url_for('greet')))
        resp.set_cookie('user_name', name)
        resp.set_cookie('user_email', email)
        return resp

    return render_template('welcome.html')


@app.route('/greet')
def greet():
    name = request.cookies.get('user_name')
    email = request.cookies.get('user_email')
    return render_template('greet.html', name=name, email=email)


@app.route('/logout')
def logout():
    resp = make_response(redirect(url_for('index')))
    resp.delete_cookie('user_name')
    resp.delete_cookie('user_email')
    return resp


if __name__ == '__main__':
    app.run()

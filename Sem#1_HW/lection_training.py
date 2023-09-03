from flask import Flask

app = Flask(__name__)

test = """
<h1>Привет, я твой пробный сайт!</h1)
,<p>Получись как надо пожалуйста! <br/>Надо чтоб быо отлично.</p>
"""
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/text/')
def text():
    return test

@app.route('/stih/')
def stih():
    zag = ['123',
           '234',
           '345',
           '567']
    txt = '<h1>Стихотворение</h1>\n<p>' + '<br/>'.join(zag) + '</p>'
    return txt

if __name__ == '__main__':
    app.run()
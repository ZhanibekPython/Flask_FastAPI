# from flask import Flask, render_template
#
#
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def main():
#     return render_template('index.html')
#
# @app.route('/about')
# def about():
#     return '<h2> О нашем сайте </h2>'
#
#
# if __name__ == '__main__':
#     app.run(debug=True)

from jinja2 import Template

# link = '''в HTML-документе ссылки определяются вот так: <a href="#">Ссылка</a>'''
# cities = [{'id': 1, 'city': 'Москва'},
#           {'id': 5, 'city': 'Тверь'},
#           {'id': 7, 'city': 'Минск'},
#           {'id': 8, 'city': 'Смоленск'},
#           {'id': 11, 'city': 'Калуга'}]
#
# link = '''<select name="cities">
# {% for c in cities -%}
# {% if c.id > 6 -%}
# <option value={{c['id']}}">{{c['city']}}</option>
# {% endif -%}
# {% endfor -%}
# </select>'''
#
# tm = Template(link)
# msg = tm.render(cities=cities)
#
#
# print(msg)

from lection_training import app

if __name__ == '__main__':
    app.run(debug=True)
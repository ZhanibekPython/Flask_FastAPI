#from jinja2 import Template, Environment, FileSystemLoader

# students = [
#     {'imya': 'John', 'course': 1, 'bdate': '01 May 2000'},
#     {'imya': 'David', 'course': 2, 'bdate': '10 March 1995'},
#     {'imya': 'Michael', 'course': 3, 'bdate': '25 December 1990'}
# ]
#
# tpl = '''
# {%- for s in clt -%}
# {% filter  %}{{s.imya}}{% endfilter %}
# {% endfor -%}
# '''

# test = Template(tpl)
# out = test.render(clt=students)
#
# print(out)

# inet = '''
# {%- macro input(name, value='', type='text', size=20) -%}
#     <input type="{{ type }}" name="{{ name }}" value="{{ value | e}}" size={{ size }}>
# {%- endmacro -%}
#
# <p>{{ input('username') }}
# <p>{{ input('email') }}
# <p>{{ input('password') }}
# '''
#
# test = Template(inet)
# test2 = test.render()
#
# print(test2)

students = [
    {'imya': 'John', 'course': 1, 'bdate': '01 May 2000'},
    {'imya': 'David', 'course': 2, 'bdate': '10 March 1995'},
    {'imya': 'Michael', 'course': 3, 'bdate': '25 December 1990'}
]

# sam = '''
# {% macro names(lst) -%}
# <ul>
# {% for i in lst -%}
#     <li>{{i.imya}} {{caller(i)}}
# {%- endfor %}
# </ul>
# {%- endmacro %}
#
# {% call(word) names(lst) %}
#     <ul>
#     <li>course: {{word.course}}
#     <li>bdate: {{word.bdate}}
#     </ul>
# {% endcall %}
# '''
#
# tst = Template(sam)
# output_ = tst.render(lst=students)
#
# print(output_)


from flask import Flask, request

app = Flask(__name__)

@app.route('/length', methods=['GET'])
def get_length():
    try:
        # Получаем строку из параметра запроса 'text'
        text = request.args.get('text')

        # Получаем длину строки
        length = len(text)

        # Возвращаем длину как ответ
        return f'Длина строки: {length} символов'
    except Exception as e:
        # Обрабатываем возможные ошибки
        return f'Произошла ошибка: {str(e)}'

if __name__ == '__main__':
    app.run(debug=True)
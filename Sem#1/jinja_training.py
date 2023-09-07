

# cars = [
#     {'model': 'Audi', 'price': 10000},
#     {'model': 'BMW', 'price': 12000},
#     {'model': 'Lada', 'price': 100}
# ]

# text = "Good cars {{ collection | replace('o', 'O') }}"
# test = Template(text)
# check = test.render(collection=cars)


# tpl = '''
# {%- for c in cars -%}
# {% filter upper %}{{c.model}}{% endfilter %}
# {% endfor -%}
# '''
#
# test = Template(tpl)
# check = test.render(cars = cars)
#
# print(check)

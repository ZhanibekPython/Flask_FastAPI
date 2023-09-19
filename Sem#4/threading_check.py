import threading
import time

import requests

urls = ['https://www.google.ru/',
        'https://gb.ru/',
        'https://ya.ru/',
        'https://www.python.org/',
        'https://habr.com/ru/all/',
        ]


def url_opener(url):
    response = requests.get(url)
    adres = 'threading_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
    with open(adres, 'w', encoding='utf-8') as src:
        src.write(response.text)
        print(f'Все норм! {time.time() - start_time}')


start_time = time.time()
threads = []
for url in urls:
    thread = threading.Thread(target=url_opener, args=[url])
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

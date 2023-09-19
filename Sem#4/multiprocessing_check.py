import time
from multiprocessing import Process

import requests

adresses = ['https://www.google.ru/',
            'https://gb.ru/',
            'https://ya.ru/',
            'https://www.python.org/',
            'https://habr.com/ru/all/',
            ]

start = time.time()


def html_creator(adres):
    request = requests.get(adres)
    name = "multproc_" + adres.replace('https://', '').replace('.', '_').replace('/', '') + ".html"
    with open(name, 'w', encoding='utf-8') as src:
        src.write(request.text)
        print(f"Процесс был выполнен за {time.time() - start}")


processes = []

if __name__ == '__main__':
    for adres in adresses:
        proc = Process(target=html_creator, args=[adres, ])
        processes.append(proc)
        proc.start()

    for proc in processes:
        proc.join()

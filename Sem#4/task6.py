import asyncio
import os

adresses = ['https://www.google.ru/',
            'https://gb.ru/',
            'https://ya.ru/',
            'https://www.python.org/',
            'https://habr.com/ru/all/',
            ]


async def word_counter(filename: str):
    with open(filename, encoding='utf-8') as file:
        text = file.read()
        print(f'Количество слов в файле {filename}: {len(text.split())}')


async def dir_processing(directory):
    tasks = []
    for file in os.listdir(directory):
        if os.path.isfile(file):
            res = asyncio.ensure_future(word_counter(file))
            tasks.append(res)
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    check_adres = r'C:\Flask_&_FastapI\Sem#4'
    asyncio.run(dir_processing(check_adres))

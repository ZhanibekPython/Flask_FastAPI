import threading
import multiprocessing
import os


def word_counter(filename: str):
    with open(filename, encoding='utf-8') as file:
        text = file.read()
        print(f'Количество слов в файле {filename}: {len(text.split())}')


def dir_processing(directory):
    threads = []
    for file in os.listdir(directory):
        if os.path.isfile(file):
            counter = threading.Thread(target=word_counter, args=[file, ])
            threads.append(counter)
            counter.start()

    for thread in threads:
        thread.join()


dir_processing(r'C:\Flask_&_FastapI\Sem#4')

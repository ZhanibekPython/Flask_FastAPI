from multiprocessing import Process, pool
import os


def word_counter(filename: str):
    with open(filename, encoding='utf-8') as file:
        text = file.read()
        print(f'Количество слов в файле {filename}: {len(text.split())}')


def dir_processing(directory):
    processes = []
    for file in os.listdir(directory):
        if os.path.isfile(file):
            res = Process(target=word_counter, args=[file, ])
            processes.append(res)
            res.start()

    for proc in processes:
        proc.join()


if __name__ == '__main__':
    dir_processing(r'C:\Flask_&_FastapI\Sem#4')

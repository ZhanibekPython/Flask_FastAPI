import argparse
import threading
from Homework_multiprocessing import time_manager, create_name, picture_download


urls = [
    'https://all.accor.com/magazine/imagerie/futuristicheskaya-astana-2-6c5e.jpg',
    'https://st2.depositphotos.com/6044446/9453/i/450/depositphotos_94539782-stock-photo'
    '-baiterek-and-architecture-of-astana.jpg',
    'https://bptrip.ru/wp-content/uploads/2014/10/astana-dostoprimechatelnosti-.jpg',
    'https://baigenews.kz/storage/storage/news/2023/01/31/mainphoto/117539/1200xauto_'
    'EwwFR57UfZ7NcXojHmCcBmuZ3ljNz0fdEPTv02jV.jpg',
    'https://e-history.kz/storage/tmp/resize/kazakhstan-history/1200_0_22116fb949fc3ba81b475b95283aab70.jpg'
]


@time_manager
def thread_test():
    threads = []
    for url in urls:
        t = threading.Thread(target=picture_download, args=[url, ])
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    # parser = argparse.ArgumentParser(description='Скрипт для скачивания изображений по заданным URL')
    # parser.add_argument('picture_download', help='Введите полный URL адрес изображения')
    # args = parser.parse_args()
    thread_test()

import multiprocessing
import time
import requests

urls = [
    'https://all.accor.com/magazine/imagerie/futuristicheskaya-astana-2-6c5e.jpg',
    'https://st2.depositphotos.com/6044446/9453/i/450/depositphotos_94539782-stock-photo-baiterek-and-architecture-of-astana.jpg',
    'https://bptrip.ru/wp-content/uploads/2014/10/astana-dostoprimechatelnosti-.jpg',
    'https://baigenews.kz/storage/storage/news/2023/01/31/mainphoto/117539/1200xauto_EwwFR57UfZ7NcXojHmCcBmuZ3ljNz0fdEPTv02jV.jpg',
    'https://e-history.kz/storage/tmp/resize/kazakhstan-history/1200_0_22116fb949fc3ba81b475b95283aab70.jpg'
]


def time_manager(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func()
        end = time.time()
        print(f'Выполнено за {end - start:.5f}')

    return wrapper


def create_name(line: str) -> str:
    """This func returns name+extension string out of URL"""
    new_name = line.split('/')[-1]
    return new_name


def picture_download(url: str):
    """This func dowloads a picture from given URL"""
    response = requests.get(url, stream=True)
    filename = create_name(url)
    try:
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
                    print(f'Все нормально, изображение {filename} загрузилось!')
    except Exception as error:
        print(f'Командир, что-то пошло не по-плану. Ошибка {error}! Разбирайся!')


@time_manager
def multproc_test():
    procs = []
    for url in urls:
        mp = multiprocessing.Process(target=picture_download, args=[url, ])
        procs.append(mp)
        mp.start()

    for proc in procs:
        proc.join()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Скрипт для скачивания изображений по заданным URL')
    parser.add_argument('picture_download', help='Введите полный URL адрес изображения')
    args = parser.parse_args()
    multproc_test()

import asyncio
import os
import time
import argparse
import aiohttp

from Homework_multiprocessing import time_manager


async def download_image(session, url, folder):
    async with session.get(url) as response:
        if response.status == 200:
            content_type = response.headers.get('content-type')
            extension = content_type.split('/')[-1]
            filename = os.path.join(folder, f"{int(time.time())}.{extension}")
            with open(filename, 'wb') as file:
                file.write(await response.read())
            return filename


@time_manager
async def main(urls, folder):
    async with aiohttp.ClientSession() as session:
        tasks = [download_image(session, url, folder) for url in urls]
        results = await asyncio.gather(*tasks)
        for result in results:
            print(f"Downloaded: {result}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Скачать изображения с заданных URL-адресов.')
    parser.add_argument('urls', metavar='URL', type=str, nargs='+',
                        help='Список URL-адресов для скачивания')
    parser.add_argument('--folder', type=str, default='images',
                        help='Папка для сохранения изображений')

    args = parser.parse_args()

    if not os.path.exists(args.folder):
        os.makedirs(args.folder)

    start_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(args.urls, args.folder))
    end_time = time.time()

    total_time = end_time - start_time
    print(f"Total time: {total_time} seconds")

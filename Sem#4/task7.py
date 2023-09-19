import random
import threading
from multiprocessing import Process
import asyncio
from random import randint
import time

lst = [random.randint(1, 101) for i in range(1000_000)]
start = time.time()


def summarizer(a):
    res = sum(a)
    print(f'Сумма {res} была высчитана за {time.time() - start:.8f}')


# threads = []
#
# for i in range(5):
#     thread = threading.Thread(target=summarizer, args=[lst, ])
#     threads.append(thread)
#     thread.start()
#
# for thread in threads:
#     thread.join()

# procs = []

# def proc_starter():
#     for i in range(5):
#         proc = Process(target=summarizer, args=[lst, ])
#         procs.append(proc)
#         proc.start()
#
#     for proc in procs:
#         proc.join()
#
#
# if __name__ == '__main__':
#     proc_starter()

import asyncio
import random
import time


def random_list(size):
    return [random.randint(1, 100) for _ in range(size)]


async def calculate_sum(arr):
    total_sum = 0
    for num in arr:
        total_sum += num
    return total_sum


async def main():
    arr = random_list(1000000)
    start_time = time.time()
    mid = len(arr) // 2
    task1 = asyncio.create_task(calculate_sum(arr[:mid]))
    task2 = asyncio.create_task(calculate_sum(arr[mid:]))

    await asyncio.gather(task1, task2)

    total_sum = task1.result() + task2.result()

    end_time = time.time()
    execution_time = end_time - start_time

    print(f"Сумма элементов массива: {total_sum}")
    print(f"Время выполнения: {execution_time} секунд")


if __name__ == "__main__":
    asyncio.run(main())
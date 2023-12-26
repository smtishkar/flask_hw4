# � Напишите программу на Python, которая будет находить
# сумму элементов массива из 1000000 целых чисел.
# � Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# � Массив должен быть заполнен случайными целыми числами
# от 1 до 100.
# � При решении задачи нужно использовать многопоточность,
# многопроцессорность и асинхронность.
# � В каждом решении нужно вывести время выполнения
# вычислений.

import asyncio
from random import randint
import time

num_tasks = 6
arr_length = 1_000_000
ttl_result = 0

async def result_calculation(arr, start_value, end_value):
    result = 0
    for i in range(start_value, end_value):
        result += arr[i]
    return result



async def main():
    global  ttl_result
    tasks = []

    for i in range(num_tasks):
        start_value = i * len(arr) // num_tasks
        end_value = (i+1) * len(arr) // num_tasks
        task = asyncio.create_task(result_calculation (arr, start_value, end_value))
        tasks.append(task)

    for task in tasks:
        ttl_result += await task
        print(ttl_result)



if __name__ == '__main__':
    start_time = time.time()
    arr = [randint(1, 100) for i in range(arr_length)]
    asyncio.run(main())
    print(f'Completed in {time.time()- start_time} seconds.')
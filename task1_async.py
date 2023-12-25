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
    print(f'Completed download in {time.time()- start_time} seconds.')
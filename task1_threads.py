# � Напишите программу на Python, которая будет находить
# сумму элементов массива из 1000000 целых чисел.
# � Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# � Массив должен быть заполнен случайными целыми числами
# от 1 до 100.
# � При решении задачи нужно использовать многопоточность,
# многопроцессорность и асинхронность.
# � В каждом решении нужно вывести время выполнения
# вычислений.



import threading
from random import randint
import time

result = 0
num_threads = 6
arr_length = 1_000_000


def result_calculation(start_value, end_value):
    global result
    for i in range(start_value, end_value):
        result += arr[i]
    print(result)


threads: list[threading.Thread] = []

def all_threads_calculation():

    for i in range(num_threads):
        start_value = i * len(arr) // num_threads
        end_value = (i+1) * len(arr) // num_threads
        thread = threading.Thread(target=result_calculation, args=(start_value, end_value))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    start_time = time.time()
    arr = [randint(1, 100) for i in range(arr_length)]
    all_threads_calculation()
    print(f'Completed in {time.time()- start_time} seconds.')
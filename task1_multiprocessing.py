import multiprocessing
from random import randint
import time

num_process = 6
arr_length = 1_000_000
ttl_result = multiprocessing.Value('i', 0)

def result_calculation(arr, start_value, end_value, result):
    for i in range(start_value, end_value):
        with result.get_lock():
            result.value += arr[i]
    print(result.value)


processes = []

def all_proc_calculation():

    for i in range(num_process):
        start_value = i * len(arr) // num_process
        end_value = (i+1) * len(arr) // num_process
        process = multiprocessing.Process(target=result_calculation,args=(arr, start_value, end_value, ttl_result))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()



if __name__ == '__main__':
    start_time = time.time()
    arr = [randint(1, 100) for i in range(arr_length)]
    all_proc_calculation()
    print(f'Completed download in {time.time()- start_time} seconds.')
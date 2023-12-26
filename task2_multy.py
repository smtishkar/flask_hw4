# Написать программу, которая скачивает изображения с заданных URL-адресов и сохраняет их на диск. Каждое изображение должно сохраняться в отдельном файле, 
# название которого соответствует названию изображения в URL-адресе.
# Например, URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
# — Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.
# — Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.
# — Программа должна выводить в консоль информацию о времени скачивания каждого изображения и общем времени выполнения программы.


import os
import multiprocessing
from pathlib import Path
import requests
import time


urls = [
'https://koshka.top/uploads/posts/2021-12/1640238679_7-koshka-top-p-kotika-srisovki-7.jpg',
'https://koshka.top/uploads/posts/2021-12/1640238618_4-koshka-top-p-kotika-srisovki-4.jpg',
'https://koshka.top/uploads/posts/2021-12/1640238637_14-koshka-top-p-kotika-srisovki-14.jpg'

]


def download_image(url):
    response = requests.get(url).content
    filename = 'multy_' + url.split('/')[-1]
    with open(filename, 'wb') as f:
        f.write(response)


processes = []


if __name__ == '__main__':
    start_time = time.time()
    for url in urls:
        process = multiprocessing.Process(target=download_image, args=(url,))
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()

    print(f'Completed download in {time.time()- start_time} seconds.')

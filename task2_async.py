# Написать программу, которая скачивает изображения с заданных URL-адресов и сохраняет их на диск. Каждое изображение должно сохраняться в отдельном файле, 
# название которого соответствует названию изображения в URL-адресе.
# Например, URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
# — Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.
# — Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.
# — Программа должна выводить в консоль информацию о времени скачивания каждого изображения и общем времени выполнения программы.


import asyncio
from asyncore import loop
import os
import multiprocessing
from pathlib import Path
import aiohttp
import requests
import time


urls = [
'https://koshka.top/uploads/posts/2021-12/1640238679_7-koshka-top-p-kotika-srisovki-7.jpg',
'https://koshka.top/uploads/posts/2021-12/1640238618_4-koshka-top-p-kotika-srisovki-4.jpg',
'https://koshka.top/uploads/posts/2021-12/1640238637_14-koshka-top-p-kotika-srisovki-14.jpg'

]


async def download_image(url):
    async with aiohttp.ClientSession() as session:
        filename = 'async_' + url.split('/')[-1]
        async with session.get(url) as response:
            img = await response.content.read()
            with open(filename, "wb") as f:
                f.write(img)

async def main():
    tasks = []

    for url in urls:
        task = asyncio.ensure_future(download_image(url))
        tasks.append(task)

    await asyncio.gather(*tasks)

if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main())

    print(f'Completed download in {time.time()- start_time} seconds.')

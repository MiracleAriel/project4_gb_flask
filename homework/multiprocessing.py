import multiprocessing
import requests
import os
import time

def download_image(url):
    response = requests.get(url)
    image_name = url.split('/')[-1]
    with open(image_name, 'wb') as f:
        f.write(response.content)
    print(f'{image_name} downloaded.')

def main_multiprocessing(urls):
    start_time = time.time()
    
    processes = []
    for url in urls:
        process = multiprocessing.Process(target=download_image, args=(url,))
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()
    
    end_time = time.time()
    print(f'Total execution time: {end_time - start_time:.2f} seconds')

if __name__ == '__main__':
    image_urls = ['https://example.com/images/image1.jpg', 'https://example.com/images/image2.jpg']
    main_multiprocessing(image_urls)

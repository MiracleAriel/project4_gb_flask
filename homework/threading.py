import threading
import requests
import os
import time

def download_image(url):
    response = requests.get(url)
    image_name = url.split('/')[-1]
    with open(image_name, 'wb') as f:
        f.write(response.content)
    print(f'{image_name} downloaded.')

def main_threading(urls):
    start_time = time.time()
    
    threads = []
    for url in urls:
        thread = threading.Thread(target=download_image, args=(url,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    end_time = time.time()
    print(f'Total execution time: {end_time - start_time:.2f} seconds')

if __name__ == '__main__':
    image_urls = ['https://example.com/images/image1.jpg', 'https://example.com/images/image2.jpg']
    main_threading(image_urls)

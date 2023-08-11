import asyncio
import aiohttp
import os
import time

async def download_image(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            image_name = url.split('/')[-1]
            with open(image_name, 'wb') as f:
                f.write(await response.read())
            print(f'{image_name} downloaded.')

async def main_asyncio(urls):
    start_time = time.time()
    
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download_image(url))
        tasks.append(task)
    
    await asyncio.gather(*tasks)
    
    end_time = time.time()
    print(f'Total execution time: {end_time - start_time:.2f} seconds')

if __name__ == '__main__':
    import aiohttp
    image_urls = ['https://example.com/images/image1.jpg', 'https://example.com/images/image2.jpg']
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main_asyncio(image_urls))

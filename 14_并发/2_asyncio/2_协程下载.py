import aiohttp
import asyncio


async def download_image(session, url):
    print("发送请求：", url)
    async with session.get(url, verify_ssl=False) as response:
        content = await response.content.read()
        file_name = url.rsplit('/')[-1]
        with open(file_name, mode='wb') as file_object:
            file_object.write(content)


async def main():
    async with aiohttp.ClientSession() as session:
        url_list = [
            'https://aisearch.cdn.bcebos.com/homepage/dashboard/ai_picture_create/01.png',
            'https://aisearch.cdn.bcebos.com/homepage/dashboard/ai_picture_create/28.png',
            'https://aisearch.cdn.bcebos.com/homepage/dashboard/ai_picture_create/29.png'
        ]
        tasks = [asyncio.create_task(download_image(session, url)) for url in url_list]
        await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())

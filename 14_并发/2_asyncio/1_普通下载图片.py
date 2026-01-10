import requests


def download_image(url):
    print("开始下载", url)
    response = requests.get(url)
    print("下载完成")
    file_name = url.rsplit('/')[-1]
    with open(file_name, mode='wb') as file_object:
        file_object.write(response.content)


if __name__ == '__main__':
    url_list = [
        'https://aisearch.cdn.bcebos.com/homepage/dashboard/ai_picture_create/01.png',
        'https://aisearch.cdn.bcebos.com/homepage/dashboard/ai_picture_create/28.png',
        'https://aisearch.cdn.bcebos.com/homepage/dashboard/ai_picture_create/29.png'
    ]
    for item in url_list:
        download_image(item)

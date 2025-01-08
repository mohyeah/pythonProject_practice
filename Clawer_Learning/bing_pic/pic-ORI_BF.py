import re
import time
import requests
from retrying import retry
from bs4 import BeautifulSoup

url = "https://cn.bing.com/images/search?q=%E7%B2%BE%E7%81%B5%E4%B8%8E%E9%BB%91%E6%9A%97%E6%A3%AE%E6%9E%97&qs=MT&form=QBIR&sp=2&lq=0&pq=%E7%B2%BE%E7%81%B5%E4%B8%8E&sk=LT1&sc=10-3&cvid=70D069363D854FA492BC17AB756815F1&first=1"
headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",

}
img_url_list = []


@retry(stop_max_attempt_number=3)   # 重试3次
def _parse_url(url):
    response = requests.get(url,headers=headers,timeout=3)
    assert response.status_code == 200  # 状态码不是200就抛出异常
    return response

def parse_url(url): # 获取网页源码
    try:
        response = _parse_url(url)
    except Exception as e:
        print("请求出错", e)
        response = None
    return response

def get_data():
    response = parse_url(url)
    if response:
        data = response.content.decode('utf-8')
        soup = BeautifulSoup(data, 'html.parser')
        # 获取img标签
        img_tags = soup.find_all('img', class_='mimg vimgld')
        for img_tag in img_tags:
            # 获取图片地址
            img_url = re.findall(r'(.*)data-src="(.*)" (.*)', str(img_tag))
            if img_url[0][1]:
                img_url_list.append(img_url[0][1])
    return img_url_list

def save_img():
    for img_url in img_url_list[:5]: # 选择下载数量
        img_data = requests.get(img_url, headers=headers,timeout=5).content
        with open(f'bing_pic-ORI_BF/{img_url[40:66]}.jpg', 'wb') as f:
            f.write(img_data)
        print(f'{img_url[40:66]}.jpg 下载成功')
        # 休眠1秒
        time.sleep(1)



if __name__ == '__main__':
    print("开始爬取数据")
    get_data()
    print("图片地址解析完毕")
    print("开始下载图片")
    save_img()
    print("下载完成")
import requests
import re
import threading


url1 = "http://127.0.0.1:9999/gdp.html"
url2 = "http://127.0.0.1:9999/index.html"

country = []
country_data = []
def get_gdp_data():
    global country
    global country_data
    data = requests.get(url1)
    data = data.content.decode("utf-8")
    data = data.split('\n')
    for line in data:
        res1 = re.findall(r"<a href=\"\"><font>(.*)</font></a>", line)
        res2 = re.findall(r"<font>\$(.*)<font>亿</font></font>", line)
        if res1:
            country.append(res1[0])
        if res2:
            country_data.append(res2[0])

    data = list(zip(country, country_data))

pic_url_list = []
def get_image():
    # 获取网页内容
    data = requests.get(url2)
    # 据.content属性获取数据
    data = data.content.decode("utf-8")

    # 对data数据解析,采集.jpg图片
    data_list = data.split('\n')
    # 遍历数据
    for line in data_list:
        res = re.findall(r'src="(.*\.jpg)"', line)
        if res:
            pic_url = "http://127.0.0.1:9999" + res[0][1:]
            pic_url_list.append(pic_url)
    return pic_url_list

def save_image():
    for i in pic_url_list:
        # 每循环一次, 模拟发送请求, 获取图片字节流数据
        pic_data = requests.get(i)
        pic_data = pic_data.content # 不用解码

        num = i.split('/')[-1]
        with open(f"./spyder/{num}", 'wb') as f:
            f.write(pic_data)

if __name__ == '__main__':
    get_gdp_thread = threading.Thread(target=get_gdp_data)
    get_image_thread = threading.Thread(target=get_image)
    save_image_thread = threading.Thread(target=save_image)

    get_gdp_thread.start()
    get_image_thread.start()
    save_image_thread.start()

    get_gdp_thread.join()
    get_image_thread.join()
    save_image_thread.join()

    print("爬取完毕")




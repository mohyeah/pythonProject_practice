import requests
import re

url = "http://127.0.0.1:9999/index.html"

pic_url_list = []
def get_image():
    # 获取网页内容
    data = requests.get(url)
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
    # 爬取图片
    pic_url_list = get_image()
    # 保存图片
    save_image()


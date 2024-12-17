import requests
import re
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif']=['SimHei']  #使用指定的汉字字体类型（此处为黑体）


'''
<a href=""><font>美国</font></a>
<font>$218463.3<font>亿</font></font>
'''

# 数据最终格式:[[], [], []]

url = "http://127.0.0.1:9999/gdp.html"

country = []
country_data = []
def get_gdp_data():
    global country
    global country_data
    data = requests.get(url)
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
    return data

def data_show():
    front_10_data = list(map(float, country_data))[:10]
    rest_20_data = sum(map(float, country_data[10:]))
    y = np.array(front_10_data + [rest_20_data])

    plt.pie(y,
            labels=country[:10]+["其他"],  # 设置饼图标签
            autopct='%1.1f%%',  # 设置百分比的格式
            explode=[0, 0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0],   #  explode:设置饼图分离的距离，为列表，列表长度与数据个数一致，默认为0，即不分离
            colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c4b5c4', '#ffb3b3', '#b3b3ff', '#b3ffb3', '#ffb3b3'],
            )
    plt.title("世界GDP前十国")  # 设置标题
    plt.show()

if __name__ == "__main__":
    get_gdp_data()
    data_show()


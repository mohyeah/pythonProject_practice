import time
import requests
import re
import bs4

url = 'https://movie.douban.com/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
}
data_list = []

# <a onclick="moreurl(this, {from:'mv_a_pst'})" href="https://movie.douban.com/subject/36498717/?from=showing">
#   <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2916584640.webp" alt="小小的我" rel="nofollow" class="">
# </a>

def get_data():
    # 获取数据
    data = requests.get(url, headers=headers)
    data = data.content.decode('utf-8')
    soup = bs4.BeautifulSoup(data, "html.parser")
    # 获取所有a标签
    a_tags = soup.find_all('a', onclick=re.compile('moreurl'))
    for a_tag in a_tags:
        # 获取所有img标签
        res = a_tag.find_all('img')
        if res:
            data_list.append(res)
    return data_list
    # [[<img alt="小小的我" class="" rel="nofollow" src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2916584640.jpg"/>], [<img alt="“骗骗”喜欢你" class="" rel="nofollow" src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2916992166.jpg"/>], [<img alt="火锅艺术家" class="" rel="nofollow" src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2916651956.jpg"/>], [<img alt="误杀3" class="" rel="nofollow" src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2916533607.jpg"/>], [<img alt="破·地狱" class="" rel="nofollow" src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2915837972.jpg"/>], [<img alt="窗前明月，咣！" class="" rel="nofollow" src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2916211653.jpg"/>], [<img alt="误判" class="" rel="nofollow" src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2916559349.jpg"/>], [<img alt="好东西" class="" rel="nofollow" src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2915454411.jpg"/>], [<img alt="雄狮少年2" class="" rel="nofollow" src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2915942528.jpg"/>], [<img alt="帕丁顿熊3：秘鲁大冒险" class="" rel="nofollow" src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2916173535.jpg"/>], [<img alt="魔法坏女巫" class="" rel="nofollow" src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2915239151.jpg"/>], [<img alt="名侦探柯南：迷宫的十字路口" class="" rel="nofollow" src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2916591242.jpg"/>], [<img alt="因果报应" class="" rel="nofollow" src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2915350868.jpg"/>], [<img alt="胜券在握" class="" rel="nofollow" src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2915237854.jpg"/>], [<img alt="狮子王：木法沙传奇" class="" rel="nofollow" src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2915201238.jpg"/>], [<img alt="角斗士2" class="" rel="nofollow" src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2914550341.jpg"/>], [<img alt="爆裂鼓手" class="" rel="nofollow" src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2915975989.jpg"/>], [<img alt="猎人克莱文" class="" rel="nofollow" src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2915773773.jpg"/>], [<img alt="完美的日子" class="" rel="nofollow" src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2914293980.jpg"/>], [<img alt="孤星计划" class="" rel="nofollow" src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2916051503.jpg"/>], [<img alt="波提切利，佛罗伦萨和美第奇家族" class="" rel="nofollow" src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2915941831.jpg"/>], [<img alt="海洋奇缘2" class="" rel="nofollow" src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2914213775.jpg"/>], [<img alt="最后的告别" class="" rel="nofollow" src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2915981188.jpg"/>], [<img alt="小倩" class="" rel="nofollow" src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2915242570.jpg"/>], [<img alt="今年二十二" class="" rel="nofollow" src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2914220139.jpg"/>], [<img alt="张杰曜北斗巡回演唱会" class="" rel="nofollow" src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2916047202.jpg"/>], [<img alt="美人鱼的夏天" class="" rel="nofollow" src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2915570843.jpg"/>], [<img alt="蓦然回首" class="" rel="nofollow" src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2914342253.jpg"/>], [<img alt="毒液：最后一舞" class="" rel="nofollow" src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2914269857.jpg"/>], [<img alt="蜡笔小新：我们的恐龙日记" class="" rel="nofollow" src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2915313612.jpg"/>], [<img alt="皇后乐队蒙特利尔现场演唱会" class="" rel="nofollow" src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2914697220.jpg"/>], [<img alt="直播惊魂夜" class="" rel="nofollow" src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2915595852.jpg"/>], [<img alt="名侦探柯南：百万美元的五棱星" class="" rel="nofollow" src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2911723556.jpg"/>], [<img alt="这个杀手不太冷" class="" rel="nofollow" src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2913554676.jpg"/>], [<img alt="海上钢琴师" class="" rel="nofollow" src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2914698334.jpg"/>], [<img alt="哈利·波特与魔法石" class="" rel="nofollow" src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2913781448.jpg"/>], [<img alt="钱来钱去" class="" rel="nofollow" src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2916008106.jpg"/>], [<img alt="哈利·波特与死亡圣器(下)" class="" rel="nofollow" src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2913457020.jpg"/>], [<img alt="哈利·波特与阿兹卡班的囚徒" class="" rel="nofollow" src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2913456870.jpg"/>], [<img alt="不想和你有遗憾" class="" rel="nofollow" src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2914748767.jpg"/>], [<img alt="哈利·波特与密室" class="" rel="nofollow" src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2913781951.jpg"/>], [<img alt="哈利·波特与火焰杯" class="" rel="nofollow" src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2913456904.jpg"/>], [<img alt="冰雪·情缘" class="" rel="nofollow" src="https://img2.doubanio.com/cuphead/movie-static/pics/movie_default_large.png"/>], [<img alt="哈利·波特与死亡圣器(上)" class="" rel="nofollow" src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2913456984.jpg"/>], [<img alt="鸳鸯楼·惊魂" class="" rel="nofollow" src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2914478954.jpg"/>], [<img alt="哈利·波特与混血王子" class="" rel="nofollow" src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2913456964.jpg"/>], [<img alt="堆塘的夏天" class="" rel="nofollow" src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2912934528.jpg"/>], [<img alt="阁楼" class="" rel="nofollow" src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2217470187.jpg"/>], [<img alt="极限守护" class="" rel="nofollow" src="https://img2.doubanio.com/cuphead/movie-static/pics/movie_default_large.png"/>]]

def save_data():
    for data in data_list[0:3]:
        pic_data = re.findall(r'<img alt="(.*)" class="" rel="nofollow" src="(.*)"/>', str(data[0]))
        pic_name = pic_data[0][0]
        pic_url = pic_data[0][1]
        pic = requests.get(pic_url, headers=headers)
        with open(f'douban_pic/{pic_name}.jpg', 'wb') as f:
            f.write(pic.content)
        time.sleep(1)

if __name__ == '__main__':
    get_data()
    save_data()
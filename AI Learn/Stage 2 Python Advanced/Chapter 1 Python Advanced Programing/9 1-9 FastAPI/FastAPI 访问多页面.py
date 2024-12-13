# 1. 导入模块
from fastapi import FastAPI
from fastapi import Response
import uvicorn

url = "C:\\Users\\ruxiang\\Desktop\\AI Learn\\00：人工智能极速就业班课程资料\\2.阶段二相关资料\\阶段二相关资料\\day17\\03-代码\\source\\blog"

# 2. 创建app对象
app = FastAPI()

# 3. 使用路由装饰器收发信息
@app.get("/" or "/index.html")
def index():
    with open(url+"\\index.html",'r') as f:
        data = f.read()

    # 返回数据给浏览器端
    return Response(data, media_type="text/html")

@app.get("/about.html")
def about():
    with open(url+"\\about.html",'r') as f:
        data = f.read()

    # 返回数据给浏览器端
    return Response(data, media_type="text/html")


# 4. 创建服务器端, 让程序一直运行
uvicorn.run(app, host="127.0.0.1", port=9990)
# 多任务型, 性能高

# 1. 导入模块
# 导入FastAPI类
from fastapi import FastAPI
# 导入Response类, 用于返回数据给浏览器端
from fastapi import Response
# 导入uvicorn服务器模块, 用于保持此文件一直运行(类似while True)
import uvicorn

# 2. 创建FastAPI对象
app = FastAPI()

# 3. 通过@app路由器收发信息
# 路由 浏览器请求 => 服务器响应对应关系

#接受浏览器发送过来的请求
@app.get("/index.html")
# 响应数据给浏览器端
def main():
    # 读取要返回的文件内
    with open("C:\\Users\\ruxiang\\Desktop\\AI Learn\\00：人工智能极速就业班课程资料\\2.阶段二相关资料\\阶段二相关资料\\day17\\03-代码\\source\\blog\\index.html",
              'r') as f:
        data = f.read()

    # 将data数据以text/html格式返回给浏览器端
    return Response(data, media_type="text/html")

# 4. 运行服务器
# 参数1: FastAPI对象
# 参数2: 绑定IP
# 参数3: 绑定端口

uvicorn.run(app, host="127.0.0.1", port=9990)

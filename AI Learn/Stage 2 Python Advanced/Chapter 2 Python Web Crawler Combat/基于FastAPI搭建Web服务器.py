from fastapi import FastAPI
from fastapi import Response
import uvicorn

app = FastAPI()

@app.get("/")
def main():
    with open("source/html/index.html", 'rb') as f:
        data = f.read()

    return Response(content=data, media_type="text/html")

# 静态页面请求通用配置
@app.get("/{path}")
def index(path: str):
    with open(f"source/html/{path}", 'rb') as f:
        data = f.read()

    return Response(content=data, media_type="text/html")

# 图片请求通用配置
@app.get("/images/{path}")  # 用户请求路径
def get_image(path: str):
    with open(f"source/images/{path}", 'rb') as f:
        data = f.read()

    return Response(content=data, media_type="image/jpeg")

uvicorn.run(app, host="127.0.0.1", port=9999)
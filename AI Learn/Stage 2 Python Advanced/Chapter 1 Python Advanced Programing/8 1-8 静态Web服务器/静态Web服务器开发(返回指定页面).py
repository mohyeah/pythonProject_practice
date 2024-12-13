import socket

if __name__ == '__main__':
    # 1.创建服务器端套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端口复用
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 2.绑定服务器地址和端口号
    tcp_server_socket.bind(("127.0.0.1", 9990))
    # 3.设置监听
    tcp_server_socket.listen(128)

    while True:
        # 4.等待客户端连接
        new_socket, ip_port = tcp_server_socket.accept()
        print(f"客户端{ip_port}已连接")

        # 5.接收客户端的请求(http请求报文)
        client_request_data = new_socket.recv(1024)

        # 过滤浏览器异常请求(浏览器关闭後, 不再接受信息)
        if client_request_data:
            client_request_data = client_request_data.decode("utf-8")


            # 将请求报文数据进行解析
            # 将请求报文数据进行切割, 分解出请求方法, 请求路径和请求协议
            request_list = client_request_data.split(" ", maxsplit=2)
            # 获取用户想要访问的资源路径
            request_path = request_list[1]

            # 判断用户请求的request_path是否为"/"
            if request_path == '/':
                request_path = "/index.html" # 默认访问首页

            # 根据请求的资源路径, 返回指定页面的数据(http响应报文)
            with open("C:\\Users\\ruxiang\\Desktop\\AI Learn\\00：人工智能极速就业班课程资料\\2.阶段二相关资料\\阶段二相关资料\\day17\\03-代码\\source\\blog"
                      + request_path, "rb") as f:   # 组装请求路径
                data = f.read() # 以rb方式读取文件数据, 在响应体中不用再转码

            # 拼接响应报文数据 => 响应行 + 响应头 + 空行 + 响应体
            response_line = "HTTP/1.1 200 OK\r\n"
            response_header = "Server: Python3.10\r\n"
            response_body = data

            response_data = (response_line + response_header + "\r\n").encode("utf-8") + response_body

            # 返回响应报文
            new_socket.send(response_data)


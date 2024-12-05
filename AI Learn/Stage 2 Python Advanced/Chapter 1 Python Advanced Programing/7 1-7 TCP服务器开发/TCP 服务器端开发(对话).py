import socket

# 1. 创建服务器端套接字对象
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# ※ 设置端口复用, 程序执行结束, 让其占用的端口可以立即释放
tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)


# 2. 绑定服务器地址和端口号
tcp_server_socket.bind(("", 9900))
# 3. 监听客户端连接
tcp_server_socket.listen(128)
while True:
    # 使用try..except捕获链接异常
    try:
        new_socket, ip_port = tcp_server_socket.accept()
        # 循环接收客户端请求 (单线程版)
        while True:
            try:
                print(f"{ip_port}客户端已连接")

                recv_data = new_socket.recv(1024).decode("utf-8")   # 接收客户端的字节流

                if len(recv_data) != 0: # 忽略空数据, 若客户端已下线, 则接收的字节流长度为0
                    print(f"{ip_port}发送的数据为:{recv_data}")
                    content = input("服务器返回数据:").encode("utf-8")
                    new_socket.send(content)
                else:
                    # 客户端已断开连接
                    raise ConnectionResetError
            except ConnectionResetError:
                print(f"{ip_port}客户端已断开")
                new_socket.close()
                break
    except:
        print("服务器异常")
        break

tcp_server_socket.close()

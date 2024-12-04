import socket

tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_server_socket.bind(("", 9900))
tcp_server_socket.listen(128)
while True:
    # 使用try..except捕获链接异常
    try:
        new_socket, ip_port = tcp_server_socket.accept()
        # 循环接收客户端请求 (单线程版)
        while True:
            try:
                recv_data = new_socket.recv(1024).decode("utf-8")
                if len(recv_data) >= 1: # 忽略空数据
                    print(f"{ip_port}发送的数据为:{recv_data}")

                    content = input("服务器返回数据:").encode("utf-8")
                    new_socket.send(content)

            except ConnectionResetError:
                print(f"{ip_port}客户端已断开")
                break
    except:
        print("服务器异常")
        break

tcp_server_socket.close()

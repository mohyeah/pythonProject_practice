import socket
# 1.创建套接字对象
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2.绑定IP地址及端口号
tcp_server_socket.bind(("", 9900))
# 3.设置监听
tcp_server_socket.listen(128)
# 4.等待客户端连接(阻塞)
while True:
    new_socket, ip_port = tcp_server_socket.accept()

# 5.接收客户端发送的数据
    recv_data = new_socket.recv(1024).decode('utf-8')
    print(f'{ip_port}发送的数据为:{recv_data}')

# 6.处理请求
    content = "copy that.".encode('utf-8')
    new_socket.send(content)

# 7.关闭套接字对象
    new_socket.close()

tcp_server_socket.close()
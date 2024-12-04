import socket
# TCP 服务器端开发七步走

# 1. 创建服务端套接字对象
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. 绑定IP地址与端口号 (本机或当前服务器)
tcp_server_socket.bind(("26.52.246.74", 9000))  # 默认绑定本机IP地址

# 3. 设置监听 (让代码监听端口号)
tcp_server_socket.listen(2)  # 允许的最大连接数,默认监听5个客户端

# 4. 等待接受客户端的连接请求
# accept() 函数会阻塞代码, 直到有客户端连接
# accept() 返回包含 新套接字对象 和 客户端信息 的元组
# 客户端与服务器端连接后, 信息的发送接受都要依靠新产生的套接字对象, 其保存了客户端与服务器端的相关信息
new_socket, ip_port = tcp_server_socket.accept()

# 5. 接受客户端发送的数据
recv_data = new_socket.recv(1024).decode('utf-8')  # 解码字节流
print(f'{ip_port}发送的数据为:{recv_data}')

# 6. 处理客户端的请求并返回数据至客户端
content = "copy that."
new_socket.send(content.encode('utf-8'))
print("数据发送完毕")

# 7. 关闭套接字对象 (新产生的连接套接字 和 服务器套接字对象)
new_socket.close()
tcp_server_socket.close()

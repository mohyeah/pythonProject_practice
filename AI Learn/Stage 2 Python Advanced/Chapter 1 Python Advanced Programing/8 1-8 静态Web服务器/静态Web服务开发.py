import socket

tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

tcp_server_socket.bind(("127.0.0.1", 9900))

tcp_server_socket.listen(128)

while True:
        # 4. 等待客户端连接 (浏览器连接)
        new_socket, ip_port = tcp_server_socket.accept()
        # 5. 接收客户端发送的数据 (返回的是HTTP请求报文)
        if new_socket:
            print(f'{ip_port}连接成功')
            client_request_data = new_socket.recv(1024).decode('utf-8')
            print(f'{ip_port}发送的数据为:\n{client_request_data}')
        # 6. 发送消息 (HTTP相应报文) => 要把数据组装成HTTP响应报文结构
            with open('index.html', 'rb') as f:
                data = f.read()     # 返回的是二进制字节流数据
            # ① 响应行
            response_line = "HTTP/1.1 200 OK\r\n"
            # ② 响应头
            response_header = "Server:PythonWeb1.0\r\n"
            # ③ 空行

            # ④ 响应体
            response_body = data
            # 组装响应报文
            response_data = (response_line + response_header + "\r\n").encode('utf-8') + response_body

            # 返回响应报文
            new_socket.send(response_data)

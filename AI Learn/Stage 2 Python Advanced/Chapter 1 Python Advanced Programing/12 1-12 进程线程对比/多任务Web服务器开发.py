# 1. 导入socket模块
import socket
import threading

# 6. 定义处理客户端请求的函数
def handle_client_request(new_socket, ip_port):
    # 7. 接收客户端发送的数据
    recv_data = new_socket.recv(1024)
    if recv_data:
        recv_data = recv_data.decode('utf-8')
        # 8. 获取用户请求的资源数据路径
        request_path = recv_data.split(' ')[1]
        if request_path == '/' or request_path == '/index.html':
            request_path = 'index.html'
        try:
            with open(request_path, "rb") as file:
                data = file.read()

        except FileNotFoundError:
            response_line = "HTTP/1.1 200 OK\r\n"
            response_header = "Server:PWB2.0\r\nContent-type:text/html; charset=utf-8}\r\n"
            response_body = "404 Not Found"

            response_data = (response_line + response_header + "\r\n" + response_body).encode("utf-8")

            new_socket.send(response_data)
        else:
            # 成功访问的文件
            response_line = "HTTP/1.1 200 OK\r\n"
            response_header = "Server: PWB2.0\r\n"
            response_body = data

            response_data = (response_line + response_header + "\r\n").encode("utf-8") + response_body
            new_socket.send(response_data)

        finally:
            # 关闭套接字
            new_socket.close()



def main():
    # 2. 创建套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端口复用
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 3. 绑定ip和端口
    server_socket.bind(("127.0.0.1", 9999))
    # 4. 设置监听
    server_socket.listen(128)
    # 5. 等待客户端连接
    while True:
        new_socket, ip_port = server_socket.accept()
        print("客户端{}已连接".format(ip_port))
        # 创建子线程
        sub_thread = threading.Thread(target=handle_client_request, args=(new_socket, ip_port))
        # 启动子线程
        sub_thread.start()



if __name__ == '__main__':
    main()
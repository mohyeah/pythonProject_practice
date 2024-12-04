import socket

# 创建一个WebServer服务器端类
class WebServer(object):
    # 初始化方法
    def __init__(self):
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server_socket.bind(("", 9090))
        self.tcp_server_socket.listen(128)

    # 处理客户端请求
    def handle_client_request(self, new_socket, ip_port):
        # 接收客户端请求
        recv_data = new_socket.recv(1024).decode('utf-8')
        print(f'客户端{ip_port}发送的数据为:{recv_data}')

        # 发送响应数据
        content = "copy, that.".encode('utf-8')
        new_socket.send(content)

        # 关闭套接字
        # new_socket.close()

    # 定义start方法,用于启动WebServer,接收客户端连接
    def start(self):
        while True:
            new_socket, ip_port = self.tcp_server_socket.accept()
            # 调用处理客户端请求方法
            self.handle_client_request(new_socket, ip_port)


# 创建程序执行入口, 实例化WebServer类生成对象
if __name__ == '__main__':
    # 实例化对象
    ws = WebServer()
    # 调用自身方法, 启动服务
    ws.start()

# 单线程 => 无法同时处理多个客户端请求,只能一个个处理
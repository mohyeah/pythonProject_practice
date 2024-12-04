import socket

# 网络调试助手 C:\Users\ruxiang\Desktop\AI Learn\00：人工智能极速就业班课程资料\2.阶段二相关资料\阶段二相关资料\day16\05-软件

# TCP客户端开发五步走:
#1.创建客户端套接字对象 socket.AF_INET => IPV4, socket.SOCK_STREAM => TCP协议
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#2.和服务端套接字建立连接
tcp_client_socket.connect(("26.52.246.74", 8000))   # 传入参数为元组

#3.向服务端发送数据 (不能是文本类型,必须是字节流数据)
while True:
    print("请输入要发送的数据:", end='')
    send_data = input()
    if send_data == "exit":
        break
    tcp_client_socket.send(send_data.encode(encoding='utf-8'))

#4.从服务端接受数据 (接受服务器端返回的数据,默认类型是字节流类型,必须进行解码)
    recv_data = tcp_client_socket.recv(1024).decode(encoding='utf-8')
    print("服务器返回数据:" + recv_data)    # 接受服务端返回的数据

#5.关闭客户端套接字
tcp_client_socket.close()







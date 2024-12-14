# 1. 进程间独立, 全局变量不互通 (父进程和子进程是独立的, 但是主进程中的全局变量是共享的)
# 2. 主进程默认不会等待子进程结束再结束, 当主进程直接结束, 子进程可能还在执行

import multiprocessing

# 创建一个全局变量(主进程中的全局变量)(主进程中的资源)
my_list = []

def write_data():
    for i in range(3):
        my_list.append(i)
        print("add:",i)
    print("write_data:{}".format(my_list))

def read_data():
    print("read_data:{}".format(my_list))

def main():
    p1 = multiprocessing.Process(target=write_data) # 创建子进程, copy一份主进程中的资源
                                                    # 对自己进程中的资源进行操作
    p2 = multiprocessing.Process(target=read_data)  # 创建子进程, copy一份主进程中的资源
                                                    # 对自己进程中的资源进行操作

    p1.start()
    p2.start()

    # 设置守护进程
    # p1.daemon = True    # 设置为守护进程, 主进程结束, 子进程也结束
    # p2.daemon = True    # 设置守护进程

    # 在主进程结束前, 强制销毁所有子进程
    #p1.terminate()
    #p2.terminate()

    # 等待子进程终止
    p1.join()
    p2.join()

    print("主进程结束")

if __name__ == '__main__':
    main()
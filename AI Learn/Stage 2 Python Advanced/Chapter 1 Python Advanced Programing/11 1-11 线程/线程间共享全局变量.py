import threading
import time

my_list = []

def add_to_list():
    for i in range(3):
        my_list.append(i)
        print("add:",i)

def read_from_list():
    print(my_list)

if __name__ == '__main__':
    t1 = threading.Thread(target=add_to_list)
    t2 = threading.Thread(target=read_from_list)

    # 共享进程内的资源
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("the end of progress")
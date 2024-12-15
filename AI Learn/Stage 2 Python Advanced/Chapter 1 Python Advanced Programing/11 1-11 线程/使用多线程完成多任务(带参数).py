# 多线程间执行是无序的，但是可以保证执行顺序

import threading
import time

def music(times, content):
    for i in range(times):
        print(content)
        time.sleep(0.2)

def coding(times, content):
    for i in range(times):
        print(content)
        time.sleep(0.2)

if __name__ == '__main__':
    t1 = threading.Thread(target=music, args=(5, "listening music"))
    t2 = threading.Thread(target=coding, kwargs={"times": 5, "content": "coding"})

    t1.start()
    t2.start()

    # 设置守护线程
    # t1.threading.Tread(target=music, args=(5, "listening music"), daemon=True)
    # 设置守护主线程
    # threading.setDaemon(True)
    # 等待两个线程执行完毕
    t1.join()
    t2.join()
    print("end of the progress")
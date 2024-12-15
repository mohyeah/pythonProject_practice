# 1. 导入模块
import threading
import time

def music():
    for i in range(10):
        print("listening music")
        time.sleep(0.2)

def coding():
    for i in range(10):
        print("coding")
        time.sleep(0.2)

if __name__ == '__main__':
    # 2. 创建线程对象
    music_thread = threading.Thread(target=music)
    coding_thread = threading.Thread(target=coding)
    # 3. 启动线程 (两者交替执行)
    music_thread.start()
    coding_thread.start()
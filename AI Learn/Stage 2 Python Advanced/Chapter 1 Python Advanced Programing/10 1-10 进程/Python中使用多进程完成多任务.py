# 多任务: 并发, 并行
# 并发: 多个任务同时执行(一段时间内交替进行)
# 并行: 多个任务同时执行(一段时间内同时进行, 任务数<CPU数)
# 进程: 运行一个程序的一个实例, 系统进行资源分配的基本单位, 进程一个进程可以有多个线程
# 线程: 同一个进程内的资源分配的最小单位

# 创建进程:
# 1. 导入进程模块
import multiprocess
import time

def music():
    for i in range(3):
        print("listening music")
        time.sleep(0.2)

def coding():
    for i in range(3):
        print("coding")
        time.sleep(0.2)

def main():
    # 2. 创建子进程
    p1 = multiprocess.Process(target=music)
    p2 = multiprocess.Process(target=coding)

    # 3. 启动进程
    p1.start()
    p2.start()
    # 4. 等待进程执行完毕
    p1.join()
    p2.join()

    print("the end")

if __name__ == '__main__':
    main()

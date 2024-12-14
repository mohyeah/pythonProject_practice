# 创建进程:
# 1. 导入进程模块
import multiprocess
import time

def music(times, t):
    for i in range(times):
        print("listening music")
        time.sleep(t)

def coding(t):
    for i in range(3):
        print("coding")
        time.sleep(t)

def main():
    # 2. 创建子进程
    p1 = multiprocess.Process(target=music, args=(3,0.2))  # 元组方式传参, 要和参数顺序保持一致
    p2 = multiprocess.Process(target=coding, kwargs={'t': 0.2}) # 字典方式传参, key和参数名保持一致

    # 3. 启动进程
    p1.start()
    p2.start()
    # 4. 等待进程执行完毕
    p1.join()
    p2.join()

    print("主进程结束")

if __name__ == '__main__':
    main()

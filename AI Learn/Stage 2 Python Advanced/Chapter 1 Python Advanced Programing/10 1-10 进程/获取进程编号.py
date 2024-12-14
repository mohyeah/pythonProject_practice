import os
import multiprocessing
import time

# 获取当前进程编号

def work():
    print("executing the work")

    # 方法1: os.getpid()

    pid = os.getpid()    # 获取当前进程编号
    print("work子进程编号:{}".format(pid))

    ppid = os.getppid()    # 获取父进程编号
    print("当前进程父进程编号:{}".format(ppid))
    time.sleep(20)

if __name__ == '__main__':
    print("主进程编号:{}".format(os.getpid()))
    sub_process = multiprocessing.Process(target=work)
    sub_process.start()



'''
#方法2: multiprocess.current_process()
pid = multiprocessing.current_process().pid
print(pid)
time.sleep(29)
'''
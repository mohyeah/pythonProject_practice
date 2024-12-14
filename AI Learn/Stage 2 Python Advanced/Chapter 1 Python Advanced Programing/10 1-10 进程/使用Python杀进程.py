import os

pid = eval(input("请输入进程编号: "))
os.kill(pid, 9) # pid 进程编号
                       # signal 信号, 与操作系统有关, 9为强制杀死进程, 15为正常结束进程

print("进程:{} is killed".format(pid))
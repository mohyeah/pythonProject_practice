import random
import time

def download(filename):
    print(f'start downloading {filename}.')
    time.sleep(random.random() * 6)
    print(f'{filename} is downloaded.')

def upload(filename):
    print(f'start uploading {filename}.')
    time.sleep(random.random() * 6)
    print(f'{filename} is uploaded.')

def record_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__} executing time:{end-start:.2f} s')
        return result
    return wrapper

download = record_time(download)
upload = record_time(upload)
download('MySQL从删库到跑路.avi')
upload('Python从入门到住院.pdf')
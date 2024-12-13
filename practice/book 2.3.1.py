import time
def test1():
    l = []
    for i in range(1000):
        l = l + [i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))

def test_time(test):
    t1 = time.time()
    for i in range(1000):
        test()
    t2 = time.time()
    print(t2-t1)

test_time(test1)
test_time(test2)
test_time(test3)
test_time(test4)


def bubble_sort(array):
    for passnum in range(len(array)-1, 0, -1):
        for i in range(passnum):
            if array[i]>array[i+1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
    return array

def short_bubble_sort(array):
    exchanges = True
    passnum = len(array)-1
    while passnum > 0 and exchanges:
        exchange = False
        for i in range(passnum):
            if array[i] > array[i+1]:
                exchange = True
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
        passnum -= 1
    return array


arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
bubble_sort(arr)
print(arr)
def insert_sort(alist):
    for index in range(1, len(alist)):

        current = alist[index]
        position = index

        while position > 0 and alist[position - 1] > current:
            alist[position] = alist[position - 1]
            position = position - 1

        alist[position] = current

    return alist

l = [888, 7, 6, 5, 4, 3, 1]
print(insert_sort(l))
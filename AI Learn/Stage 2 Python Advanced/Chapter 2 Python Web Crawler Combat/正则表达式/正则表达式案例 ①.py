import re

'''
匹配列表中特定的元素
'''

list1 = ["apple", "banana", "cherry", "duff"]

str1 = str(list1)

res = re.finditer(r"(apple|duff)", str1)

for i in res:
    print(i.group())

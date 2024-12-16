import re

str1 = "hello python, hello java"

# 选择匹配符
# | 表示或
result = re.finditer(r"hello (python|java)", str1)

if result:
    for i in result:
        print(i.group())
else:
    print("no match")
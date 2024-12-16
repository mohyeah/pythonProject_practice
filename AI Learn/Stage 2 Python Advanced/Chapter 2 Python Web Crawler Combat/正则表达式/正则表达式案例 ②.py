import re

'''
匹配邮箱信息
'''

email = "1478670@qq.com, go@126.com, heima123@163.com"

res = re.finditer("\w+@(qq|126|163)\.com", email)

if res:
    for i in res:
        print(i.group())
else:
    print("没有匹配到")

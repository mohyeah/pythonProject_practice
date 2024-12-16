import re

'''
正则中的split
切分QQ号
'''

str1 = "qq:10567"
str2 = "abc1243efg456hij"
str3 = "Apple banana"

res1 = re.split(":", str1)
res2 = re.split(r"\d{3}", str2)
res3 = re.search(r"(apple|banana)", str3, flags=re.I)

print(res1)
print(res2)
print(res3.group())
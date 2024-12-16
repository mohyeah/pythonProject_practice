import re

str1 = "aBBCCd1234efg1221hijk1111lmnopqrst"

res1 = re.search(r"\d\d\d\d", str1)
# 反向引用, 匹配连续四个数字,
res2 = re.search(r"(\d)\1\1\1", str1)
# 匹配1221
res3 = re.search(r"(\d)(\d)\2\1", str1)
# 匹配AABB
res4 = re.search(r"([A-Z])\1([A-Z])\2", str1)

print(res1.group())
print(res2.group())
print(res3.group())
print(res4.group())

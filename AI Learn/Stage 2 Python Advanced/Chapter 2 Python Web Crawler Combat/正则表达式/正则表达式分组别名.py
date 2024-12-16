import re

str1 = "<book></book>"

# (?P<name>)  为分组起别名
# (?P=name)   引用别名为name分组匹配到的字符串

res = re.search(r"<(?P<tag>\w+)></(?P=tag)>", str1)

print(res.group())
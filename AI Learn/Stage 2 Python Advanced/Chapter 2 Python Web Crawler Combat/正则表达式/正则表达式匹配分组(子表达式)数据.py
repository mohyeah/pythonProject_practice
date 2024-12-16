import re

# 定义一个字符串, 匹配字符串中的123, 并单独获取2,3
str1 = "abcdef123ghijklmn"

# 若正则中带有分组(子表达式)数据, 用search或finditer获取数据
res = re.search(r"\d(\d)(\d)", str1)    # 匹配字符串中的123, 并单独获取2,3, 存储在缓冲区中
                                               # r表示原生字符串(rawstring),该字符串声明了引号中的内容表示该内容的原始含义，避免了多次转义造成的反斜杠困扰。
# 匹配成功後, 产生3个结果, 分别是: 匹配到的字符串, 分组1, 分组2
print(res.group())  # result.group()
print(res.group(1)) # result.group(缓冲区号)
print(res.group(2)) # result.group(缓冲区号)

f = float(input("please input temp:"))
c = (f - 32)/1.8
print("%.1fF = %.1fC"%(f, c))
print(f'{f:.1f}华氏度 = {c:.1f}摄氏度') # f-string用大括号 {} 表示被替换字段，其中直接填入替换内容

def toStr(n, base):
    '''
    进制转换
    :param n: 数
    :param base: 进制位
    :return:
    '''
    convertString = '01234567890ABCDEF'
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base, base) + convertString[n % base]

print(toStr(100,16))
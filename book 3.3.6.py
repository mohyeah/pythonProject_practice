class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

def base2_Converter(decNumber):
    '''
    十进制转换为二进制
    :param decNumber: 十进制数
    :return: 二进制数
    '''
    remstack = Stack()
    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2
    binString = ""
    while not remstack.isEmpty():
        binString += str(remstack.pop())
    return binString

def baseConverter(decNumber, base):
    '''
    十进制转X进制
    :param decNumber: 十进制数
    :param base: X进制
    :return: X进制数
    '''
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    binString = ""
    while not remstack.isEmpty():
        binString += digits[remstack.pop()]
    return binString

print(base2_Converter(10))
print(baseConverter(10,16))
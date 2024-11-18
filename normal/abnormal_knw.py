# 自定义异常
class SELF_DEF_EXCEPTION(Exception):
    def __init__(self, message, context=None):
        super().__init__(message)
        self.context = context

def calculater(num1, op, num2): # 定义函数calculater，接收三个参数num1, op, num2
    match op:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            try:
                return num1 / num2
            except ZeroDivisionError as e:  # 捕获除数为0的异常
                # 手动引发异常
                raise SELF_DEF_EXCEPTION('不能除0')    # 返回自定义的异常信息

            except ValueError as e:
                raise SELF_DEF_EXCEPTION('invalid number')    # 返回异常信息

        case '%':
            return num1 % num2
        case '**':
            return num1 ** num2
        case _:
            return 'Invalid operator'

num1 = eval(input('Enter an number: '))
op = input('Enter an operator: ')
num2 = eval(input('Enter another number: '))
cal1 = calculater(num1, op, num2)
print(cal1)



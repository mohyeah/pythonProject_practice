def gcd(m, n):
    # 代码清单1-6 化简分数
    while m%n != 0:
        old_m = m
        old_n = n
        n = old_n
        m = old_m%old_n
    return n

class Fraction:
    '''
    分数
    '''
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    def show(self):
        print(str(self.numerator) + '/' + str(self.denominator))
    def __str__(self):
        return str(self.numerator) + '/' + str(self.denominator)
    def __add__(self, other):
        ''' 两分数相加 '''
        new_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        # 求最大公约数
        common = gcd(new_numerator, new_denominator)
        # 化简
        new_numerator = new_numerator // common
        new_denominator = new_denominator// common
        if new_denominator == 1:
            return new_numerator
        else:
            return Fraction(new_numerator, new_denominator)
    def __eq__(self, other):
        # 深相等
        first_numerator = self.numerator * other.denominator
        second_numerator = self.denominator * other.numerator
        return first_numerator == second_numerator

myf = Fraction(3, 5)
myf.show()
print(myf)
print('I have ate %s pizza' % myf)
f1 = Fraction(3, 5)
f2 = Fraction(6, 15)
print(f1 + f2)
print(f1 == f2)
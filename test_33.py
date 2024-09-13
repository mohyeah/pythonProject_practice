class Triangle(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and a + c > b and b + c > a

    '''
    @classmethod
    def is_valid(cls, a, b, c):
        return a + b > c and a + c > b and b + c > a
    '''
    def perimeter(self):
        return self.a + self.b + self.c
    def area(self):
        p = self.perimeter() / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

t1 = Triangle(1, 1, 1)
print(t1.perimeter())
print(t1.area())
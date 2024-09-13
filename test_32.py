class Student:
    __slots__ = ('name', 'age')
    def __init__(self, name, age):
        self.name = name
        self.age = age

stu = Student('aff', 20)
stu.sex = 'male'
print(stu.sex)
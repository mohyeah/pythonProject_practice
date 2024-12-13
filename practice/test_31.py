class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def study(self, course_name):
        print(f'{self.__name} is {course_name}')

stu = Student('Lily', 20)
stu.study('Python')
print(stu._Student__name)
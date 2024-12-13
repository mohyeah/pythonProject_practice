class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print(f'studying {course_name}.')

    def play(self):
        print(f'playing...')

stu1 = Student('Patrick', 10)
stu2 = Student('John', 20)

stu1.study('Python')
stu2.play()
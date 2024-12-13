class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name} is eating')
    def sleep(self):
        print(f'{self.name} is sleeping')

class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
    def study(self, course_name):
        print(f'{self.name} is studying {course_name}')
class Teacher(Person):
    def __init__(self, name, age, title):
        super().__init__(name, age)
        self.title = title
    def teach(self, course_name):
        print(f'{self.name} is teaching {course_name}')

stu1 = Student('Bob', 21)
stu2 = Student('Jack', 25)
tea1 = Teacher('Pob', 21, title='Python')
stu1.eat()
stu2.sleep()
tea1.eat()
stu1.study('Python')
tea1.teach('Python')
stu2.study('C++')
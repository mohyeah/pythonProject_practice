class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age
    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, age):
        self._age = age
    def play(self):
        if self._age < 16:
            print(f'{self._age}is playing')
        else:
            print(f'{self._age}is not playing')

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade
    @property
    def grade(self):
        return self._grade
    @grade.setter
    def grade(self, grade):
        self._grade = grade
    def study(self, course):
        print(f'{self._name} is studying {course}')


def main1():
    person = Person('John', 18)
    person.play()
    person.age = 22
    person.play()
if __name__ == '__main__':
    main1()
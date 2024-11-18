class Car(object):
    pass

car = Car()

class Dog:
    def __init__(self, name, age, sex="male"):
        self.name = name
        self.age = age
        self.sex = sex

    def run(self):
        print("{} is running".format(self.name))

    def speak(self, sound):
        print(f"{self.name} is speaking:\"{sound}!\"")

'''
d1 = Dog('Bob', 12)
d2 = Dog('Tom', 10, 'female')
d3 = Dog('Jerry', 8)
print("my dog name is {0}, {2}, {1} years".format(d1.name, d1.age, d1.sex))
print("my dog name is {0}, {2}, {1} years".format(d2.name, d2.age, d2.sex))
d3.run()
d3.speak('wolf')
'''


class Account:
    interest_rate = 0.005   #类变量, //因与个体无关,用类名来调用
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    #类方法
    @classmethod
    def interest_by(cls, amt):
        return cls.interest_rate * amt
act1 = Account('Bob', 1000)
print(Account.interest_by(act1.amount))

class Animal:

    def __init__(self, name):
        self.name = name

    def show_info(self):
        return "name: {}".format(self.name)

    def move(self):
        return "{} is moving".format(self.name)
class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

cat = Cat('Tom', 3)
print(cat.move())
print(cat.show_info())



# 多继承
class Horse:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        return "name of horse:{}".format(self.name)

    def run(self):
        print("Horse {} is running".format(self.name))

class Donkey:
    def __init__(self, name):
        self.name = name
    def show_info(self):
        return "name of donkey:{}".format(self.name)
    def run(self):
        print("Donkey {} is running".format(self.name))
    def roll(self):
        print("Donkey {} is rolling".format(self.name))

class Mule(Horse, Donkey):  #多继承下,方法冲突下,遵循继承的先后顺序
    def __init__(self, name, age):  #继承父类属性
        super().__init__(name)
        self.age = age

    def show_info(self):    #重写父类方法
        return "Mule: {0}, {1} years.".format(self.name, self.age)

Mu1 = Mule('Mu1', 3)
Mu1.run()
Mu1.roll()
print(Mu1.show_info())


# 继承与多态
class Boat:
    def hook(self):
        print("Boat is hooking")

class Ship(Boat):
    def hook(self):
        print("Ship is Wuuuuuuing")

class Destroyer(Boat):
    def hook(self):
        print("Destroyer is bombing")
'''
B1, S1, D1 = Boat(), Ship(), Destroyer()
B1.hook()
S1.hook()
D1.hook()
'''
# 鸭子类型测试
def start(obj):
    obj.speak()

class Car:
    def speak(self):
        print("Car is hooking")

start(Car())
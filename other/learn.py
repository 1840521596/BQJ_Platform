# coding=utf-8
class Person:
    """
    封装
    """

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def eat(self):
        print("%s,%s岁,%s,吃饭" % (self.name, self.age, self.gender))

    def drink(self):
        print("%s,%s岁,%s,喝水" % (self.name, self.age, self.gender))

    def sleep(self):
        print("%s,%s岁,%s,睡觉" % (self.name, self.age, self.gender))


if __name__ == '__main__':
    a = Person('jack', 10, '男')
    a.eat()
    a.drink()
    a.sleep()

    b = Person('rose', 11, '女')
    b.eat()
    b.drink()
    b.sleep()


class Animal:
    """
    封装
    """

    def __init__(self, name):
        self.name = name

    def eat(self):
        print("%s 吃 " % self.name)

    def drink(self):
        print("%s 喝 " % self.name)

    def shit(self):
        print("%s 拉 " % self.name)

    def pee(self):
        print("%s 撒 " % self.name)


class Cat(Animal):
    """
    继承
    """

    def cat_cry(self):
        print('%s 喵喵哭' % self.name)

    def cat_eat(self):
        self.eat()


class Dog(Animal):
    def bark(self):
        print('%s 汪汪叫' % self.name)


if __name__ == '__main__':
    c1 = Cat('猫one')
    c1.eat()
    c1.drink()
    c1.shit()
    c1.pee()

    c2 = Cat('猫two')
    c2.cat_eat()
    c2.drink()
    c2.cat_cry()

    d1 = Dog('狗one')
    d1.eat()
    d1.bark()



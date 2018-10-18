# # coding=utf-8
# class Person:
#     """
#     封装
#     """
#
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def eat(self):
#         print("%s,%s岁,%s,吃饭" % (self.name, self.age, self.gender))
#
#     def drink(self):
#         print("%s,%s岁,%s,喝水" % (self.name, self.age, self.gender))
#
#     def sleep(self):
#         print("%s,%s岁,%s,睡觉" % (self.name, self.age, self.gender))
#
#
# if __name__ == '__main__':
#     a = Person('jack', 10, '男')
#     a.eat()
#     a.drink()
#     a.sleep()
#
#     b = Person('rose', 11, '女')
#     b.eat()
#     b.drink()
#     b.sleep()
#
#
# class Animal:
#     """
#     封装
#     """
#
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self):
#         print("%s 吃 " % self.name)
#
#     def drink(self):
#         print("%s 喝 " % self.name)
#
#     def shit(self):
#         print("%s 拉 " % self.name)
#
#     def pee(self):
#         print("%s 撒 " % self.name)
#
#
# class Cat(Animal):
#     """
#     继承
#     """
#
#     def cat_cry(self):
#         print('%s 喵喵哭' % self.name)
#
#     def cat_eat(self):
#         self.eat()
#
#
# class Dog(Animal):
#     """
#     继承
#     """
#     def bark(self):
#         print('%s 汪汪叫' % self.name)
#
#
# if __name__ == '__main__':
#     c2 = Cat('猫one')
#     c2.cat_eat()
#     c2.drink()
#     c2.cat_cry()
#
#     d1 = Dog('狗one')
#     d1.eat()
#     d1.bark()
#
#

# import json
#
#
# def json_out(indent=None, sort_keys=False):
#     def actual_decorator(decorated):
#         def inner(*arg, **kw):
#             result = decorated(*arg, **kw)
#             return json.dumps(result, indent=indent, sort_keys=sort_keys)
#         return inner
#     return actual_decorator
#
#
# @json_out(indent=5)
# def json_nothing():
#     return {'a': 2, "b": 3}
#
#
# print(json_nothing())


def reverse(x):
    if -10 < x < 10:
        return x
    n = abs(x)  # 都按正数进行操作
    str1 = str(n)
    if len(str1) > 10:
        return 0

    v = ''
    for i in range(len(str1)):
        v += str1[-(i + 1)]
    result = int(v)
    if x < 0:
        result = -result
    if -2147483648 < result < 2147483647:
        return result
    else:
        return 0


if __name__ == '__main__':
    print("请输入数字：")
    x = int(input())
    print(reverse(x))

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
#         print("%s,%s岁,%s,吃奶" % (self.name, self.age, self.gender))
#
#     def he(self):
#         print("%s,%s岁,%s,喝水" % (self.name, self.age, self.gender))
#
#     def shui(self):
#         print("%s,%s岁,%s,睡觉" % (self.name, self.age, self.gender))
#
#
# if __name__ == '__main__':
#     a = Person('jack', 10, '男')
#     a.eat()
#     a.he()
#     a.shui()
#
#     b = Person('rose', 11, '女')
#     b.eat()
#     b.he()
#     b.shui()
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
#     def cry(self):
#         self.name = '猫'
#         print('%s 喵喵哭' % self.name)
#
#
# class Dog(Animal):
#     def cry(self):
#         self.name = "狗"
#         print('汪汪叫')
#
#
# # if __name__ == '__main__':
# #     c1 = Cat('猫one')
# #     c1.eat()
# #
# #     c2 = Cat('猫two')
# #     c2.drink()
# #
# #     d1 = Dog('狗one')
# #     d1.eat()
import json

import requests

param = {'registerId': 'null'}
work_id = 'YZ201809071028344488'
rq = requests.get('https://www.bqj.cn/order/original/info/' + work_id, params=param)
result = rq.text
number = json.loads(result)
print(type(number))
print("数字"+number['copyright']['bqjCheckNum'])

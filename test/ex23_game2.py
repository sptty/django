# -*- coding:utf-8 -*-
# __author__ = 'sean'
# Fri Mar  9 14:38:31     2018

class Animal:
    def eat(self):
        print("%s吃." % self.name )

    def drink(self):
        print("%s喝." % self.name)

    def shit(self):
        print("%s拉." % self.name)

    def pee(self):
        print('%s撒' % self.name)

class Cat(Animal):
    def __init__(self, name):
        self.name = name
        self.breed = '猫'

    def cry(self):
        print("喵喵喵")

class Dog(Animal):
    def __init__(self, name):
        self.name = name
        self.breed = '狗'

    def cry(self):
        print('汪汪汪')


cat1 = Cat('张玉家的猫猫')
cat1.eat()

dog1 = Dog('万洪波家的松狮')
dog1.pee()


# python 继承多个类

class Wolf(Animal, Cat, Dog): #
    def __init__(self, name):
        self.name = name
        self.breed = '狼'

wolf1 = Wolf('天上上的狼')
wolf1.cry()




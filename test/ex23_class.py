# coding:utf-8
# __author__ = 'Sean'

# 创建类
class Foo:
    def bar(self, name):
        print("this is the first class."+ name)

Foo1 = Foo()


Foo1.bar('name')


class person:
    def tall(self, name, high):
        print("My name is " + name + ',and I am tall ' + high )

    def girl(self, name, girl_name):
        print("My name is " + name + ",My girl friend's name is " + girl_name)

wan = person()
wan.tall('wan','175')
wan.girl('wan','Sean yu')



class book:
    def __init__(self, name ,weight):
        self.name = name
        self.weight = weight

ob1 = book('santi','sun')
print(ob1.name)


class c1:
    def print1(self):
        print('print a string.')

    def argv1(self, name):
        print('I am %s' % name)


obj1 = c1()
obj1.print1()
obj1.argv1('wan')

obj2 = book('wan', 'test')

print(obj2.name)
print(obj2.weight)




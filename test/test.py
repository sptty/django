# -*- encoding:utf-8 -*-
#


# def fei(max):
#     list1 = []
#     n,a,b = 0,0,1
#     while n < max:
#         # b = a + b # 第一个数
#         list1.append(b)
#         #print(b)
#         # x =a
#         # a = b
#         # b += x
#         a,b = b, a+b
#         n += 1
#     return list1
#
# for i in fei(100000):
#     print(i)
#

#
# class Fei(object):
#
#     __doc__ = "this is a test. "
#
#     def __init__(self,max):
#         self.max = max
#         self.n, self.a, self.b = 0, 0, 1
#
#     def __iter__(self):
#         return self
#
#     def next(self):
#         if self.n < self.max:
#             r = self.b
#             self.a ,self.b = self.b ,self.b + self.a
#             self.n = self.n + 1
#             return r
#         raise StopIteration()
#
#
# for n in Fei(1000000000):
#     print n



def feb(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a+b
        n += 1

for i in feb(10):
    print(i)


import inspect
print inspect.isgeneratorfunction(feb)
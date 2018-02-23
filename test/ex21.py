# coding:utf-8
# __author = 'sean'
# date Thu Feb  8 14:35:30 CST 2018

# from sys import argv
# scripts, str_1, str_2 = argv

str_1 = raw_input("please input first number:" )  # raw_input 输入的是字符串，input是数值
str_2 = raw_input("please input second number:" )
print(type(str_1))
def add(a, b):
    print("adding %r + %r " % (a, b))
    return a + b

def plus(a, b):
    print("plus %d * %d " % (a, b))
    return a * b

def minus(a, b):
    print("minus %d - %d " % (a, b))
    return a - b

def divide(a, b):
    print("divide %d / %d" % (a, b))
    return a/b

def multi(a, b):
    print("this is a multi function : %d * %d + %d - %d " % (a,b,a,b))
    return a*b+a-b

num_1 = float(str_1)
num_2 = float(str_2)

print(add(num_1, num_2))
print(plus(num_1, num_2))
print(minus(num_1, num_2))
print(divide(num_1, num_2))
print(multi(num_1, num_2))

# coding:utf-8
# __author__ = 'sptty'
# date  Mon Jan 29 17:44:14 CST 2018


def cheese_and_crackers(cheese_count, boxes_of_crackers):   # 定义函数名称和变量名称
    print("You have %d cheeses!" % cheese_count)    #输出第一个函数
    print("You have %d boxes of crackers!" % boxes_of_crackers) # 输出第二个函数
    print("Man that's enough for a party!") #打印一句话
    print("Get a blanket.\n")

print("We can just give the function numbers directly:")

cheese_and_crackers(20,40)


print("Or we can use variables from our scripts:")
amount_of_cheese = 10
amount_of_crackers = 20

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10+20,30+34)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese+10, amount_of_crackers+20)

from ex18 import check_list4

def fun_in_fun():
    a = {'avc':'wewe'}
    check_list4(**a)

fun_in_fun()


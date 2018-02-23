# coding:utf-8
# __author = 'sptty'
# Mon Jan 22 17:44:14 CST 2018

# this one is like your scripts with argv.
def print_two(*args):
    arg1, arg2 = args
    print("arg1 : %r, arg2 : %r" % (arg1, arg2 ))

# Ok that *argv is actually pointless, we can just do this.
def print_two_again(arg1, arg2):
    print("arg1 : %r, arg2 : %r" % (arg1, arg2))

# just take one argv
def print_one(arg1):
    print("arg1 : %r " % arg1)

# this one takes no arguments
def print_none():
    print("I got nothing")

print_two("Wan","Sean")
print_two_again("Wan2","Sean2")
print_one('Wan3')
print_none()



def check_list(*args):
    arg3, arg4= args
    print(str(type(args)))
    for i in args:
        print(i)
    print("the first argv is %r, the second argv is %r" % (arg3,arg4))
    print("there are the argv %r  %r" % args)

check_list("ewe","rwrw")

def check_list2(arg5,arg6):
    print("the first argv is %r, the second argv is %r" % (arg5, arg6))
#
from sys import argv
script,name = argv
check_list2(script,name)



def check_list3(*args3): #此时把argv传递进来的变量当成列表，*args3 ，则是当成元祖歘传递进来
    print(str(type(args3)))
    for i in args3:
        print(i)
    print("the first argv is %r, the second argv is" % str(args3))

c3 = ('a','b','v')
check_list3(c3)
check_list3(1,2,3,4)


def check_list4(**args4): #此时把argv传递进来的变量当成列表，*args3 ，则是当成元祖歘传递进来
    print(str(type(args4)))
    for i in args4:
        print(i)
    print("the first argv is %r, the second argv is" % args4)

c4={'a':'c'}
check_list4(**c4)
check_list3(*c4)


from ex19 import cheese_and_crackers


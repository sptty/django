# -*- coding:utf-8 -*-
#
# author: sptty
# date:20180613

people = 30
cars = 40
buses = 15

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("we should not take the cars.")

if buses > cars:
    print("That's too many buses.")
elif buses < cars:
    print("Maybe we could take the buses.")
else:
    print("We still can't decide")

if people > buses:
    print("alright.let's just take the buses.")
else:
    print("fine,let's stay home then.")

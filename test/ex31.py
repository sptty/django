# -*- coding:utf-8 -*-
# author: sptty
# date

print("you enter a dark room with two doors. do you go through door #1 or door #2 ?")

door = raw_input("> ")

if door == "1":
    print("There is a giant bear here eating a cheese cake. what do you do ?")
    print("1. take the cake.")
    print("2. scream at the bear.")

    bear = raw_input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job.")
    elif bear == "2":
        print("the bear eats your legs off. Good job.")
    else:
        print("Well,doing %s is probably better, Bear runs aways.") % bear

elif door == "2":
    print("you stare into the endless abyss at cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. understanding revolvers yelling melodies.")

    insanity = raw_input("> ")

    if insanity == "1"  or insanity == "2":
        print("Your body survives powered by a mind of jello. Good job.")
    else:
        print("the insanity rots your eyes into a pool of muck. Good job.")
else:
    print("You stumble around and fall on a knife and die. Good job.")

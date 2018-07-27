# -*- coding:utf-8 -*-
# author = ''
# date :
#


from sys import exit


def gold_room():
    # 金屋，这个房间都是金子
    print("This room is full of gold,How much do you take ? ")

    next = raw_input('> ')
    if '0' in next or '1' in next:
        how_much = int(next)
    else:
        dead("you greedy bastard! ")

    if how_much < 50:
        print("Nice,you are not greedy,you win.")
        exit(0)
    else:
        dead("you greedy bastard! ")


def bear_room():
    # 告诉你这是熊的房间，熊的后面有一扇门，怎么到门那里呢
    print("There is a beae here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")

    bear_moved = False

    while True:
        next = raw_input(">")
        print(type(next))

        if next == "take money":
            dead("the bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print("the bear has moved from the door, you can go through it now.")
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead('The bear gets pissed off and chows your legs off.')
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    # 火云邪神的房间
    print("here you see the great evil cthulhu.")
    print("He, it, whatever stares at ypi add ypi gp insane.")
    print("do you flee for your life or eat your head.")

    next = raw_input('> ')

    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty !")
    else:
        cthulhu_room()


def dead(why):
    print(why,"Good job!")
    exit(0)


def start():
    # 游戏开始
    print("you are in a dark room.")
    print('there is a door to your right and left.')
    print('which one do you take ?')

    next = raw_input('> ')

    if next == 'left':
        bear_room()
    elif next == 'right':
        cthulhu_room()
    else:
        dead('you stumble around the room until you starve.')


start()



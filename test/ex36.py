# -*- coding:utf-8 -*-
#author:
#date
#

from sys import exit

def get_out_fail():
    print('I am so sorry, re-input again.')

def get_out_ok():
    print('you are a wise man ,now you can get those.')
    print('congratulation！！！')
    result_status = True
    return result_status


def get_reward():
    print('U r a good emplee. give 5k RMB.')
    exit(0)


def gold_room():
    print('you are so true,so i give some gold, how much do you want?')
    choice_gold = raw_input('> ')
    if int(choice_gold) > 50:
        print(u'你太贪婪了，没收你的美女。')
        print('*********离开房间*********梦醒了-----')
        # get_out_fail()
        exit(7)
    elif int(choice_gold) <= 50:
        print('you are so 聪明，你可以拿走这些,再见祝你好运。')
        exit(0)


def enter_dream():
    second_choice = False

    while True:
        print('I am the leader of all beauty, now you are entering my dream.')
        print('do you want a beauty girl? ')
        choice_beauty = raw_input('> ')

        if choice_beauty == 'yes' and not second_choice :
            print('you are a bad man. kick your ass.')
            get_out_fail()
            second_choice = True
        elif choice_beauty == 'no':
            print('you are a xu wei man .')
            get_out_fail()
        elif choice_beauty == 'yes' and second_choice:
            print('You a true man，this beauty belongs to you now')
            gold_room()
            return False
            # continue
        else:
            print('I do not know what you say ,so kill you.')
            exit(8)



def find_a_letter():
    print('one morning,you walk at the gate of the company mall,and see a letter.')
    print('do you want to open the letter or left on the front-desk? open or not? ')
    open_or_not = raw_input(' > ')

    if open_or_not == 'no':
        print("you are very lucky. because this is the CEO'letter ,if you open, you are fired.")
        get_reward()   # 获得奖励
    else:
        print('你的眼前闪现大量的烟雾，出来一个美女。')
        enter_dream()
    # elif open_or_not == 'open':
    #     enter_dream()
    # else:
    #     print('I do not know what you want.just type in open or no.')
    #     get_out_fail()


def start_game():
    result_status = False
    while not result_status:
        find_a_letter()
        enter_dream()


start_game()


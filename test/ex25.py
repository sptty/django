# -*- coding:utf-8 -*-
# __author__ = 'sean'
# Tue Apr 25 16:27:26     2018


import pdb
def break_word(stuff):
    """this function will break words for us ."""
    words = stuff.split(' ')
    return words


def sort_word(words):
    """sort the words."""
    return sorted(words)


def print_first_word(words):
    """print the first word after popping it off."""
    word_1 = words.pop(0)
    return word_1


def print_last_word(words):
    """print ths last word after popping it off."""
    # print('print last word: '+str(type(words)))
    word = words.pop(-1)
    return word


def sort_sentence(sentence):
    """Take in a full sentence and returns the sorted words."""
    words = break_word(sentence)
    return sort_word(words)


def print_first_and_last_word(sentence):
    """sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print(print_first_word(words))
    print(print_last_word(words))
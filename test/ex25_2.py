# -*- coding:utf-8 -*-
# __author__ = 'sean'
# Tue Apr 25 16:27:26     2018

from ex25 import *
import pdb
import sys,os
sentence = "In this exercise, we’re going to interact with your .py fi le inside the python interpreter you used"

words = break_word(sentence)
words = sort_word(words)

print(print_first_word(words))
# pdb.set_trace()
print(print_last_word(words))
print_first_and_last_word(sentence)


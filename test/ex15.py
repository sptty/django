# -*- coding:utf-8 -*-
#

from sys import argv
scripts,filename = argv
new_filename = 'ex15_example.txt'
txt = open(filename)
print("The scripts name is %s :") % scripts
print("Here is you file %r :") % new_filename

print txt.read()

print "Type the filename again:"
file_again=raw_input("[root @localhost ~] ")
txt_again = open(file_again)

print txt_again.read()


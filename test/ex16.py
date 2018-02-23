# coding:utf-8
#__author__ = 'sptty'
#

from sys import argv
import time

script, filename = argv

print("We're going to erase %r." % filename)
print("If you don't want that .hit CTRL-C (^C)")
print("If you do want that ,hit RETURN.")

raw_input("?")

print("Opening the file...")
target = open(filename,'w+')

print("Truncating the file. Goodbye ")
target.truncate()

print("Now I.m going to ask you for three lines.")

line1 = raw_input('line 1:')
line2 = raw_input('line 2:')
line3 = raw_input('line 3:')

print('I am going to write those to the file.')

target.write(line1 + '\n' + line2 +'\n' + line3 )
# target.write(line1)
# target.write('\n')
# target.write(line2)
# target.write('\n')
# target.write(line3)
# target.write('\n')

print('And finally,We close it.\n\n\n\n')
# target.close()
#
# # # time.sleep(5)
#
# target = open(filename,'r')
# print(str(target))
# target.truncate()
for i in target.readlines():
    print(i)
target.close()

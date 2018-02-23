# __author__ = 'sptty'
# coding:utf-8
from sys import argv

script,user_name = argv
prompt = 'root@localhost >  '

print "Hi,%s I am the %s script." %(user_name,script)
print "I'd like to ask you a few questions."

print "Do you like me ? %s" % user_name
likes = raw_input(prompt)

print "Where do you live ? %s" % user_name
lives = raw_input(prompt)

print "what kind of computer do you have ?%s" %user_name
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.""" % (likes,lives,computer)

print """
actually,you name is %s,and you have word %s to me,because you stole my computer %s.
""" % (likes,lives,computer)
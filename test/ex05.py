# -*- coding: utf-8 -*-

name = 'Zed.'
age = 35 # not a lik
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brain'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy" % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes,hair)
print "his teeth are usually %s depending on the coffee." % teeth

# this line is tricky,try ti get it exactly right.

print "If I add %d ,%d, and %d I get %d ," %(
    age,height,weight,age + height + weight)

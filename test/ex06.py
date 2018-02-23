# -*- coding:utf-8 -*-
#

# this is a string with variables
x = "There are %d types of people." % 10

binary = "binary" # this is a string
do_not = "don't" # this is a string
y = "Those who know %s and those who %s." % (binary, do_not)

print x # print the variables
print y # print the variables

print "I said: %r ." % x #print a string
print "I also said: '%s'." % y  # print a  string

# hilarious = False  # give hilarious with a variables
hilarious = True  # give hilarious with a variables

# give a variables with a string value.
joke_evalution = "Isn't that joke so fuuny?! %r"

print joke_evalution % hilarious #print the results after string calculate a  Bool string

w = "This is the left side of .." # give a string with a variables
e = "a string with right side."  # give a  string with a  variables

print w + e     #print to two string together.

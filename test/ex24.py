# -*- coding:utf-8 -*-
# __author__ = 'sean'
# Tue Apr 24 16:27:26     2018

print('Let\'s practice everything .')
print("You'd need to know about escapes with \\ that do \n newlines and \t tabs.")

poem = """
\t The lovely world 
with logic so firmly planted
cannot discern  \t the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\t where there is none.
"""


print "- - - - - - - - - - - - - - "
print(poem)
print "- - - - - - - - - - - - - - "


five = 10 -2 + 3 - 6
print("this should be five %d " % five)


def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    creates = jars / 500
    return jelly_beans, jars, creates


start_point = 10000
beans, jars, creates = secret_formula(start_point)

print("with a starting point of: %d" % start_point)
print("we'd have %d beans,%d jars, and %d creates." % (beans, jars, creates))

start_point /= 10

print("we can also do that this way:")
print("we'd have %d beans,%d jars, and %d creates." % secret_formula(start_point))

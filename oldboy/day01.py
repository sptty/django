__auth__ = 'sptty'
import sys
real_num = 143

guess_num = 0

while real_num != guess_num:

    guess_num = int((raw_input('Input the number:'))

    # if type(guess_num) != type(1):
    #   print('%s is not a number,Please input a number.' % guess_num)
    #   sys.exit()

    if real_num > guess_num:
            print('Please input bigger number')
    elif real_num < guess_num:
            print('Please input smaller number.')
    else:
            print('congratultions,you got it ! ')
            sys.exit()

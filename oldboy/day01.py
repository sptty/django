__auth__ = 'sptty'
import random

# real_num = 143
real_num = random.randrange(10)
guess_num = 0

count = 0
for i in range(0,3):
# while True:
#    if count >3:
    # print('You have already testing more than 10 times !')

    # guess_num = int(input('Input the number:'))
    guess_num = str(input('Input the number:')).strip()

    # guess_num = int(guess_num)

    # print(test1)
    if len(guess_num) == 0:
        print('Please input the number again! not space or Enter')
        continue
    elif guess_num.isdigit():
        guess_num = int(guess_num)
        # count += 1
    else:
        print('Please input the <number> again! not alpha and alnum')
        continue

# if type(guess_num) != type(1):
    #   print('%s is not a number,Please input a number.' % guess_num)
    #   sys.exit()

    if real_num > guess_num:
            print('Please input bigger number')
    elif real_num < guess_num:
            print('Please input smaller number.')
    else:
            print('congratulations,you got it ! ')
            # sys.exit()
            break
else:
    print('You have already reach limit of 3 times !')
    print('wah a pity ! The real number is %s' % real_num)

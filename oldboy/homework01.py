# -*- coding:utf-8 -*-

import os,sys,re


def info_index():
    __doc__ = '输入用户名和密码'
    name=raw_input('Input your name:')
    password=raw_input('Input your password:')
    new_info_user = str(name+','+password)
    return new_info_user


'''
def all_user_name_list():
    correct_name = []
    with open('./day01_databases.txt') as user_databases:
        for line in user_databases.readlines():
            # print(line)
            correct_name.append(line.split(',')[0])
        # print(correct_name)
        # print(type(correct_name))
        correct_name=tuple(correct_name)
        # print(correct_name)
        # print(type(correct_name))
        return correct_name
'''



def all_user_name_password_times_list():
    __doc__ = '获取文件中所有的正确的用户名密码和输入错误次数'
    with open('./day01_databases.txt') as user_databases:
        correct_name_password_times = []
        for line in user_databases.readlines():
            correct_name_password_times.append(line)          # 这里的correct_name_password_times列表，但是调用的时候，return的整个列表值就变成了元组中的第一个元素，
            user_databases.close()
            # correct_name_password.append(line.split(',')[0-2])
        # print(correct_name_password_times)
        # print(type(correct_name_password_times))
        return correct_name_password_times


# def write_user_databases(*correct_name_password_times):
#     __doc__ = '将输入密码的用户，记录他们输错的次数，并写入文件'
#     for i in correct_name_password_times:  # 这一步的作用跟之前一样，凡是函数传递的元组都这样处理
#         # print('i  '+ str(i)+ str(type(i)))
#         correct_name_password_times = list(i)
#         # print('correct_name_password_times  '+ str(correct_name_password_times)+ str(type(correct_name_password_times)))
#
#     for i in range(0, len(correct_name_password_times)):
#         #  将用户信息逐行写入新文件，在替换原来原件
#         user_databases = open('./.day01_databases.txt.tmp', 'a')
#         # print(str(correct_name_password_times[i]))
#         user_databases.write(correct_name_password_times[i])
#         user_databases.close()
#         # else:
#         # user_databases = open('./.day01_databases.txt.tmp', 'w')
#     os.remove('./day01_databases.txt')
#     os.rename('./.day01_databases.txt.tmp', './day01_databases.txt')


def judge_user_name(new_info_user,*correct_name_password_times):
    __doc__ = '判断用户名，密码和输入次数是否禁止登录'
    new_name,new_password=new_info_user.split(',')          #

    for i in correct_name_password_times:
        correct_name_password_times=list(i)
    # correct_name_password_times = list(correct_name_password_times)[0]
    # 其实这个元组也只有一个元素，所以这里写成correct_name_password_times=list(correct_name_password_times)[0]也是可以的

    # print('correct_name_password_times' + ' is ' + str(type(correct_name_password_times)) + str(correct_name_password_times))
    # for i in correct_name_password_times:
    #   print(i)


    all_correct_name=[]
    # 获取所有正确的用户用于后面比对新用户是否存在
    for i in range(0,len(correct_name_password_times)):
        all_correct_name.append(correct_name_password_times[i].split(',')[0])
        # print('correct_name    '+str(correct_name))


    # for i in range(0,len(correct_name_password_times)):
    #     correct_name,correct_password,correct_times=correct_name_password_times[i].split(',')
    #     print(str(type(correct_password))+correct_password)
    #     print(str(type(correct_times))+correct_times)

    if new_name in all_correct_name:
        # 判断是否存在正确用户名
        # print('the user ' + new_name + ' is  exist  1111111111!')
        new_name_status=0
    else:
        # print('the user ' + new_name + ' is not  exist 1111111!')
        new_name_status=1

    def write_user_databases(*correct_name_password_times):
        __doc__='将输入密码的用户，记录他们输错的次数，并写入文件'
        for i in correct_name_password_times:   # 这一步的作用跟之前一样，凡是函数传递的元组都这样处理
            # print('i  '+ str(i)+ str(type(i)))
            correct_name_password_times=list(i)
            # print('correct_name_password_times  '+ str(correct_name_password_times)+ str(type(correct_name_password_times)))

        for i in range(0, len(correct_name_password_times)):
            #  将用户信息逐行写入新文件，在替换原来原件
            user_databases = open('./.day01_databases.txt.tmp', 'a')
            # print(str(correct_name_password_times[i]))
            user_databases.write(correct_name_password_times[i])
            user_databases.close()
            # else:
                # user_databases = open('./.day01_databases.txt.tmp', 'w')
        os.remove('./day01_databases.txt')
        os.rename('./.day01_databases.txt.tmp','./day01_databases.txt')


    if new_name_status==0:
        # 表示用户存在则执行下面的代码
        for i in range(0,len(correct_name_password_times)):

            correct_name,correct_password,correct_times=correct_name_password_times[i].split(',')
            # 逐个获取正确的用户名。密码。输入次数  进行判断
            if new_name == correct_name:
                # 用户名正确先判断是否禁用，然后判断密码是否正确，最后如果密码输入错去则调用之前的 write_user_databases函数更新输入次数
                # print('the user ' + new_name + ' is  exist !')
                # print(correct_name+correct_password+correct_times)
                if int(correct_times) >=3:
                    print(new_name + ' forbidden to login!')
                elif new_password == correct_password:
                    print('welcome' + ',' + new_name + ', login successful!!')
                else:
                    print('the user ' + new_name + ' password is not correct !')
                    correct_times=int(correct_times)+1
                    correct_name_password_times[i]=correct_name+','+correct_password+','+str(correct_times)+'\n'
                    # print('correct_name_password_times[i]'+correct_name_password_times[i])
                    # password_is_not_correct=0
                    # print('correct_times is ' + str(correct_times))

                    # return new_name+correct_times
                    write_user_databases(correct_name_password_times)

                # else:
            #     print('the user ' + new_name + ' is not  exist !')
    else:
        print('the user ' + new_name + ' is not  exist, system is logining out ......')
        # 提示用户不存在，退出系统



# 输入密码次数思路
# 将所有用户密码文件读入变量中，在关闭文件
# 在循环变量，在覆盖写入源文件

'''
        else:
            print('the user ' + new_name + ' is not exist !')


            return False
        else:
            print('the user ' + new_name + ' is OK !')
            return new_name,new_password


def judge_user_password(new_info_user,correct_name_password):
    new_name, new_password = new_info_user.split(',')
    if new_info_user in correct_name_password:
        print('welcome'+','+new_name+', login successful!!')
        return True
    else:
        print('the user ' + new_name + ' password is not correct !')
        return new_name


def forbidden_user_login(new_info_user,new_name):
    with open('day01_databases.txt','a') as f:
        line = f.readlines()
        for i in line:
            correct_name,correct_password,count=i.split(',')

            if  new_name == correct_name and count<=3:
                new_count=int(count)+1
                i.replace(','+str(count),','+str(new_count))
                f.writelines(i)
                f.close()
                break

            elif new_name == correct_name and count>=3:
                print(new_name + ' forbidden to login!')
                break

'''


if __name__=='__main__':
    new_info_user=info_index()
    # correct_name=all_user_name_list()
    correct_name_password_times=all_user_name_password_times_list()
    # print('correct_name_password_times' + ' is ' + str(type(correct_name_password_times)) + str(correct_name_password_times))
    # for i in range(0,len(correct_name_password_times)):
    #    print(correct_name_password_times[i])

    judge_user_name_results=judge_user_name(new_info_user,correct_name_password_times)

    # print('judge_user_name_results'+' is '+str(type(judge_user_name_results))+str(judge_user_name_results))
    # forbidden_user_login(new_info_user,correct_name)

'''
    if judge_user_name_results is False:
        print('Do you want to sign up this user ?')
        pass
    else:
        for i in tuple(judge_user_name_results):
            judge_user_name_results=tuple(i)
            # print('judge_user_name_results' + ' is ' + str(type(judge_user_name_results)) + str(judge_user_name_results))
'''







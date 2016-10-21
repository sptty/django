# -*- encoding:utf-8 -*-
#
#     要求：
#     1.开发员工信息查询程序，可以支持模糊查询员工信息
#     2.匹配到的员工信息，需高亮显示，并且显示匹配条数
#     3.支持员工信息的增删改查
#     4.用户在启动程序后，可以不断的循环查询
#
#     信息表素材：staff.txt

import os

def user_choice():

    def user_choice_input(choice_num):
        try:
            count=0
            while not (int(choice_num) >= 1 and int(choice_num) <= 5):
                choice_num=raw_input(u'输入错误,请输入数字,您的选择序号(0-5):')
                count+=1
                if count>=3:
                    choice_num=5
                    print('您输错次数已超过3次，系统即将退出......')
                    return choice_num
        except ValueError:
            print('您的输入非数字，系统即将退出......')
            choice_num=5

        return choice_num

    print('员工查询系统菜单：\n1.增加员工信息\n2.修改员工信息\n3.查询员工信息\n4.删除员工信息\n5.退出查询系统')

    choice_num = raw_input(u'请输入您的选择序号(0-5):')
    choice_num=user_choice_input(choice_num)
    return choice_num


def input_staff_info():
    new_staff_name = raw_input(u'请输入姓名：  ')
    new_staff_job = raw_input(u'请输入职称:  ')
    new_staff_dept = raw_input(u'请输入部门:  ')
    new_staff_tel = raw_input(u'请输入手机号码:  ')
    new_staff_email = raw_input(u'请输入电子邮箱:  ')
    new_staff_info=new_staff_name + ',' + new_staff_job + ',' + new_staff_dept + ',' + new_staff_tel + ',' + new_staff_email+'\n'
    return new_staff_info


def all_staff_info():
    all_staff_info_list=[]
    with open('./day01_user_info.txt','r') as  all_staff_info:
        for i in all_staff_info.readlines():
            print(i)
            all_staff_info_list.append(i)

    return all_staff_info_list


def new_all_staff_info(*extra_staff_info):
        # all_staff_info_list = []
        with open('./day01_user_info.txt', 'r') as  all_staff_info:
            all_staff_info_list=list(all_staff_info)
            # print('all_staff_info_list:' + str(all_staff_info_list) + str(type(all_staff_info_list)))
            for i in extra_staff_info:
                all_staff_info_list.append(i+'\n')
            # print('all_staff_info_list'+str(type(all_staff_info_list)))
                return all_staff_info_list


def write_to_files(*new_all_staff_info):

    with open('./.day01_user_info.txt.tmp', 'a') as  all_staff_info_tmp:
        for i in new_all_staff_info:
            for j in i:
                all_staff_info_tmp.write(j)
    all_staff_info_tmp.close()

    os.remove('./day01_user_info.txt')
    os.rename('./.day01_user_info.txt.tmp', './day01_user_info.txt')


def staff_search():
    pass

def staff_modify():
    pass

def staff_delete():
    pass

def staff_display():
    pass

def staff_info():
    pass

def modify_staff_info():
    pass

def exit_judge(user_choice):
    if int(user_choice) == 5:
        return True
    else:
        # print('不退出执行')
        return False



if __name__=='__main__':
    print('----------------Staff information query system-------------------')

    exit_status=False

    while not exit_status:                           # 循环执行

        user_choice_num = int(user_choice())             # 获取用户输入的数字
        EXIT_JUDGE = exit_judge(user_choice_num)     # 判断是否退出,值为True和False
        if EXIT_JUDGE:
            break

        if   user_choice_num == 1:
            print('1.增加员工信息')
            new_staff_info=input_staff_info()

            all_staff_info_list=all_staff_info()
            if new_staff_info in all_staff_info_list:
                print('The information of new staff '+ new_staff_info.split(',')[0]+' is exist.Please re-inout new staff information.')
            else:
                new_all_staff_info_list=new_all_staff_info(new_staff_info)
                write_to_files(new_all_staff_info_list)

        elif user_choice_num == 2:
            print('2.修改员工信息')

        elif user_choice_num == 3:
            print('3.查询员工信息')

        elif user_choice_num == 4:
            print('4.删除员工信息')




    print('-----------------------Logging out system------------------------')




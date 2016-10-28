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
    new_staff_info='\n'+new_staff_name + ',' + new_staff_job + ',' + new_staff_dept + ',' + new_staff_tel + ',' + new_staff_email
    return new_staff_info


def all_staff_info():
    all_staff_info_list=[]
    with open('./day01_user_info.txt','r') as  all_staff_info:
        for i in all_staff_info.readlines():
            # print(i)
            all_staff_info_list.append(i)

    return all_staff_info_list


def new_all_staff_info(method=('add','del'),*extra_staff_info):
        # all_staff_info_list = []
        with open('./day01_user_info.txt', 'r') as  all_staff_info:
            all_staff_info_list=list(all_staff_info)
            # print('all_staff_info_list:' + str(all_staff_info_list) + str(type(all_staff_info_list)))
            for i in extra_staff_info:
                if method == 'add':
                    all_staff_info_list.append(i)
                # print('all_staff_info_list'+str(type(all_staff_info_list)))
                elif method == 'del':
                    print(str(i))
                    print(all_staff_info_list)
                    all_staff_info_list.remove(i)
                # else:
                #     print('Please choice the method add or del.')

            return all_staff_info_list


def write_to_files(*new_all_staff_info):

    with open('./.day01_user_info.txt.tmp', 'a') as  all_staff_info_tmp:
        for i in new_all_staff_info:
            for j in i:
                all_staff_info_tmp.write(j)
    all_staff_info_tmp.close()

    os.remove('./day01_user_info.txt')
    os.rename('./.day01_user_info.txt.tmp', './day01_user_info.txt')


def staff_search(staff_key_info,*all_staff_info_list):
    __doc__='传入查询关键子和所有用户信息，通过输入的每个关键字进行信息匹配'
    # for i in all_staff_info_list:
    #     all_staff_info_list=i
    print('staff_search_info'+str(type(all_staff_info_list))+str(all_staff_info_list))
    print('staff_key_info'+str(type(staff_key_info))+str(staff_key_info))



    staff_key_name,staff_key_job,staff_key_dept,staff_key_tel,staff_key_email=staff_key_info.split(',')
    staff_key_info=[staff_key_name,staff_key_job,staff_key_dept,staff_key_tel,staff_key_email]
    # print(staff_key_name,staff_key_job,staff_key_dept,staff_key_tel,staff_key_email,staff_key_info)

    staff_search_results_tmp=[]

    for i in range(0, len(staff_key_info)):                                   # 循环遍历查询关键字
        # print('staff_key_info'+','+staff_key_info[i]+','+str(type(staff_key_info[i])))
        if len(staff_key_info[i]) == 0:                                             # 如果输入为空，遍历下一个关键字
            # print('None')
            continue
        for j in range(0,len(all_staff_info_list)):                           # 循环遍历所有用户信息
            # print('staff_key_info' + '\n' + staff_key_info[i])
            # print('all_staff_info_list' + '\n' + str(type(list(all_staff_info_list[j])))+all_staff_info_list[j])
            all_staff_info_list[j]=list(all_staff_info_list[j].split(','))
            # for k in range(0, len(all_staff_info_list[j])):
            #     print(all_staff_info_list[j][k])
            for k in range(0,len(all_staff_info_list[j])):                    # 循环遍历每个用户的所有信息，进行匹配
                # print('all_staff_info_list[j][k]' + all_staff_info_list[j][k])
                # print(all_staff_info_list[j][k])
                # if staff_key_info[i].strip() in all_staff_info_list[j][k]:     #将各个列的关键字进行匹配,支持精确匹配
                if staff_key_info[i].strip() in all_staff_info_list[j][k]:       #将各个列的关键字进行匹配,支持模糊匹配
                    # print(staff_key_info).
                    # staff_search_results=staff_search_results+','+all_staff_info_list[j]
                    staff_search_results_tmp.append(all_staff_info_list[j])         # 返回搜索结果
                    # print(staff_search_results)

    staff_search_results=''
    for i in range(0,len(staff_search_results_tmp)):
        if i==len(staff_search_results_tmp)-1:
            staff_search_results=staff_search_results+str(staff_search_results_tmp[i])
            print(staff_search_results_tmp[i])
        else:
            staff_search_results=staff_search_results+str(staff_search_results_tmp[i]+',')

        print(staff_search_results)
        print('staff_search_results')
        return staff_search_results








# new_staff_info = '\n' + new_staff_name + ',' + new_staff_job + ',' + new_staff_dept + ',' + new_staff_tel + ',' + new_staff_email


def staff_modify():
    pass

def staff_delete():
    pass

def staff_display(*staff_search_results):
    for i in staff_search_results:
        staff_search_results=i
        for j in staff_search_results:
            print(u'搜索结果如下：'+'\n'+str(j))

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
        EXIT_JUDGE = exit_judge(user_choice_num)     # 判断是否退出,值为True和False,
        if EXIT_JUDGE:                              # 如EXIT_JUDGE为True，则退出循环
            break

        if   user_choice_num == 1:
            print('1.增加员工信息')
            new_staff_info=input_staff_info()

            all_staff_info_list=all_staff_info()
            if new_staff_info.strip()+'\n' in all_staff_info_list:      #
                print('The information of new staff '+ new_staff_info.strip().split(',')[0]+' is exist.Please re-inout.')
            else:
                new_all_staff_info_list=new_all_staff_info('add',new_staff_info)
                write_to_files(new_all_staff_info_list)

        elif user_choice_num == 2:
            print('2.修改员工信息')



        elif user_choice_num == 3:
            print('3.查询员工信息')
            staff_key_info=input_staff_info()
            all_staff_info_list=all_staff_info()
            staff_search_results=staff_search(staff_key_info,all_staff_info_list)
            staff_display(staff_search_results)


        elif user_choice_num == 4:
            print('4.删除员工信息')

            staff_key_info=input_staff_info()
            all_staff_info_list=all_staff_info()
            staff_search_results=staff_search(staff_key_info,all_staff_info_list)
            # for i in staff_search_results:
            #     staff_search_results=staff_search_results[0]
            # for i in all_staff_info_list:
            #     all_staff_info_list=all_staff_info_list[0]
            print('staff_search_results\n'+str(type(staff_search_results))+str(staff_search_results))
            print('all_staff_info_list\n'+str(type(all_staff_info_list[0]))+str(all_staff_info_list))

            if not all_staff_info_list.__contains__(staff_search_results):
                print('The information of new staff '+ staff_key_info.strip().split(',')[0]+' is not  exist.Please re-inout.')
            else:
                print('4.删除员工信息-----------')
                new_all_staff_info_list=new_all_staff_info('del',staff_search_results)
                write_to_files(new_all_staff_info_list)

            # staff_search_results=staff_search(staff_key_info,all_staff_info_list)
            # staff_display(staff_search_results)




    print('-----------------------Logging out system------------------------')




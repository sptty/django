# coding:utf-8
# from sys import argv
# script,volume = argv
import sys

def type_count():
    ''' type_count 返回 shop_num,already_install,shop_mirror_num,pre_install,beijing,chongqing,shanghai,shenzhen
    data = type_count(), data[x],x序号表示：
    0电频谱数量，
    1已安装数，
    2店家镜面总数，
    3原装总数,
    4北京，
    5重庆，
    6上海，
    7深泽店家数，'''
    already_install = 0
    pre_install = 0
    shop_mirror_num = 0
    shop_num = 0
    shanghai = 0
    beijing = 0
    chongqing = 0
    shenzhen = 0
    shop_sgined = 0
    shop_stoped = 0

    f = open('mirror.txt','r')  # 打开数据文件，4列，分别为城市，已安装数，店家屏幕数，预计安装数

    for i in f.readlines():
        list_i = list(i.split())
        # print(str(list_i))
        if list_i[0] == '北京':
            beijing += 1
        if list_i[0] == '重庆':
            chongqing += 1
        if list_i[0] == '上海':
            shanghai += 1
        if list_i[0] == '深圳':
            shenzhen += 1
        if list_i[1] == '审核通过':
            shop_sgined += 1
            # 按照正在合作的店铺屏幕数量
            # already_install += int(list_i[2])
            # pre_install += int(list_i[3])
            # shop_mirror_num += int(list_i[4])
            # shop_num += 1
        else:
            shop_stoped += 1

        # 开发过得所有屏幕数量
        already_install += int(list_i[2])
        pre_install += int(list_i[3])
        shop_mirror_num += int(list_i[4])
        shop_num += 1

    f.close()

    return shop_num,already_install,shop_mirror_num,pre_install,beijing,chongqing,shanghai,shenzhen,shop_sgined,shop_stoped


all_data = type_count()

# print(type_count.__doc__)

# print('\n')
# print('*'*40)
print(u"到目前为止，店铺数据分析如下：")
print('*'*40)
print(u"已签约店家数量： %d" % all_data[8])
print(u"已终止店家数量： %d" % all_data[9])
print('*'*40)
print(u"已签约店家总量： %d" % all_data[0])
print(u"已安装屏幕总量： %d" % all_data[1])
print(u"预安装屏幕总量： %d" %  all_data[2])
# print(u"平均每家店安装量： %f" % (already_install/shop_num))
print(u"店铺屏幕总量： %d" % all_data[3])


print('*'*40)
print('\n')


# coding:utf-8
# from sys import argv
# script,volume = argv


already_install = 0
pre_install = 0
shop_mirror_num = 0
shop_num = 0

f = open('mirror.txt','r')  # 打开数据文件，三列，分别为已安装数，店家屏幕数，预计安装数

for i in f.readlines():
    list_i = list(i.split())
    #print(str(list_i))
    already_install += int(list_i[0])
    pre_install += int(list_i[1])
    shop_mirror_num += int(list_i[2])
    shop_num += 1

f.close()

print('\n')
# print('*'*40)
print(u"到目前为止，店铺数据分析如下：")
print('*'*40)
print(u"已签约店家总量： %d" % shop_num)
print(u"已安装屏幕总量： %d" % already_install)
print(u"预安装屏幕总量： %d" %  shop_mirror_num)
#print(u"店铺有屏幕总量： %f" % (already_install/shop_num))
print(u"平均每家安装量： %d" % pre_install)

print('*'*40)
print('\n')

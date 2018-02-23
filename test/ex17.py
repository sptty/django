# coding:utf-8
# __author__ = 'Sean'
# Date Fri Jan 19 10:59:47 CST 2018

from sys import argv
from os.path import exists
from time import timezone
script, out_file, in_file = argv

print("copying data from %s to %s" % (out_file,in_file))

out_txt = open(out_file)
out_data = out_txt.read()
# 判断输入字符长度
# print(type(out_data) , str(type(len(out_data))))
# print(out_data)
print("The input file is %d bytes long" % len(out_data))

# 判断写入文件是否存在
print("Dos the output file exists? %r" % exists(in_file))

print("Ready,hit the RETURN to continue ,CTRL-C to abort.")
raw_input("Continue?")

in_txt = open(in_file,'a')
in_txt.write(out_data+'\n')

print("All right.")

out_txt.close()
in_txt.close()

# out_data = open(out_file,'r').read()
# with open(out_file,'r') as out_data:
#     print("The input file is $d bytes long" % len(out_data))
#     out_data.read()
#     out_data.close()




# 下面是我自己看题写的
# from sys import argv

# script, out_file, in_file = argv
#
# out_txt = open(out_file,'r')
# in_txt = open(in_file,'a')
#
# in_txt.write(out_txt.read())
#
# out_txt.close()
# in_txt.close()
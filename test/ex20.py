# coding:utf-8
from sys import argv    # import module .

script,input_file = argv    # 变量赋值

def print_all(f):   # 定义函数，功能读取文件的一行
    print(f.read())

def rewind(f):      # 将读取行数指针指到最开始的地方
    f.seek(0)


def print_a_line(line_count, f):    # 输出打印第几行和这行的内容。
    # print(line_count,f.readline())
    # print("this is the " + str(line_count) + " lines.")
    print("the context is : " + f.readline())

current_file = open(input_file) # 打开文件

print("First let's print the whole file.\n")
print_all(current_file)   # 打印所有内容

print("Now let's rewind .kind of like a tape.")
rewind(current_file)    # 将读取指针只会最开始地方，不然下面所有的内容都输出为空

print("Let's print three lines:")

current_line = 1  # 初始第一行
print_a_line(current_line, current_file)    # 调用函数，导出第几行和指针在的位置行内容


current_line += 1
print_a_line(current_line, current_file)


current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)



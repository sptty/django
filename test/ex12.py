# -*- coding:utf-8 -*—
y = raw_input('你多大了啊？')
# x=type(y)
# print(type(y),x)
while y !='int':
    y = raw_input('请输入整数\n你多大了啊？')
print('你现在都'+str(y)+'岁了啊，我见你的时候才'+str((int(y)-16))+'岁!!!真是岁月不饶人啊~~~')
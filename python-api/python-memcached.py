# -*- coding:utf-8 -*-
#
# 
# 如果没有memcache的package,
# 需要先pip install memcache 即可

import memcache

mc = memcache.Client(['10.1.166.51:11211'],debug=0)

for i in range(1,160000):
    mc.set('key'+str(i),'value'+str(i))
    print(i)


#!/usr/bin/env python
#

import memcache

mc = memcache.Client(['10.1.166.51:11211'],debug=0)

for i in range(60000,160000):
    mc.set('key'+str(i),'value'+str(i))
    print i

# encoding: utf-8
import os,sys
# with open(r'E:\\03.devops\\AI\\a.txt','a') as  f:
#     for i in range(1,100,2):
#         f.write('testtttttttttttttttttt\n'+str(i))
#     # print(f.read())
#     f.close()
# try:
#     import cPickle as pcikle
# except ImportError:
#     import pickle


try:
    import cPickle as pickle
except ImportError:
    import pickle

d = dict(url='index.html',title='首页',content='first_page')
# print(str(pickle.dumps(d)))
pickle.dumps(d)
f = open(r'E:\\03.devops\\AI\\a.txt','ab')
pickle.dump(d,f)
f.close()

f = open(r'E:\\03.devops\\AI\\a.txt','rb')
d = pickle.load(f)
f.close()
print(d['title'])

    # with open(r'E:\\03.devops\\django\\README.md','w') as filereader:
    # filereader.write('test')

    #for line in filereader.readlines():
      # print line
      #   print(str(filereader.read()))


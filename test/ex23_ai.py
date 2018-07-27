# -*- coding:utf-8 -*-
# __author__ = 'sean'
# date Wed Mar 28 16:10:27     2018


# from sklearn import svm
#
# X = [[0, 0], [1, 1], [1, 0]]  # training samples
# y = [0, 1, 1]  # training target
# clf = svm.SVC  # class
# clf.fit(X, y)  # training the svc model
# result = clf.predict([2, 2]) # predict the target of testing samples
# print result  # target


import count
import matplotlib.pyplot as plt

data = count.type_count()

labels_1 = u'beijing', u'chongqing', u'shanghai', u'shenzhen'
counts_1 = data[4], data[5], data[6], data[7]
colors_1='yellowgreen','gold','lightskyblue','red'
#print(str(type(colors)))
explode_1=0,0.1,0,0
plt.pie(counts_1,explode=explode_1,labels=labels_1,colors=colors_1,autopct='%1.2f%%',shadow=True,startangle=50)
plt.axis('equal')
plt.show()

labels_2 = 'shop_signed','shop_stoped'
counts_2 = data[8],data[9]
colors_2 = 'yellowgreen','red'
explode_2 = 0,0.1
plt.pie(counts_2,explode=explode_2,labels=labels_2,colors=colors_2,autopct='%1.2f%%',shadow=True,startangle=50)
plt.axis('equal')
plt.show()

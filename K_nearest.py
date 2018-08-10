# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 15:13:26 2018

@author: prince khera
"""

from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import warnings
from collections import Counter

style.use('fivethirtyeight')

def distance(xs,ys):
    d = 0
    for i,j in zip(xs,ys):
        d+=(i-j)**2
    return sqrt(d)

def k_nearest(data,predict,k=3):
    if len(data) >= k:
        warnings.warn('k is less than total no. of groups')
    d = []
    for i in data:
        for ii in data[i]:
            di = distance(ii,predict)
            d.append([di,i])
    r = [i[1] for i in sorted(d)[:k]]
    return Counter(r).most_common(1)[0][0]

d = {'k':[[1,2],[1,3],[2,3]],'r': [[4,5],[4,6],[5,5]]}
p = [1,1]

[[plt.scatter(ii[0],ii[1],s=50,color=i) for ii in d[i]] for i in d]
c = k_nearest(d,p,k=3)
plt.scatter(p[0],p[1],s=100,color=c)


p = [2,3]

x = [1,2]
y = [1,2]
d = distance(x,y)
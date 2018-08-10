# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 16:32:12 2018

@author: prince khera
"""

from math import sqrt
import numpy as np
import warnings
from collections import Counter
import pandas as pd
import random

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
    return Counter(r).most_common(1)[0][0], Counter(r).most_common(1)[0][1]/k


df = pd.read_csv('breast_cancer.txt',names=['id','clump_thickness','unif_cell_size','unif_cell_shape','marg_adhesion','single_epith_cell_size', 'bare_nuclei','bland_chrom','norm_nucleioli','mitoses','class'])
df.replace('?',-99999,inplace=True)
df.drop(['id'],1,inplace=True)

data = df.astype(float).values.tolist()
random.shuffle(data)
test_size = 0.2

d_train = {}
for i in data[:-int(test_size*len(data))]:
    d_train[i[-1]] = d_train.get(i[-1], [])
    d_train[i[-1]].append(i[:-1])


d_test = {}
for i in data[-int(test_size*len(data)):]:
    d_test[i[-1]] = d_test.get(i[-1], [])
    d_test[i[-1]].append(i[:-1])

c = 0
t = 0
for i in d_test:
    for ii in d_test[i]:
        if k_nearest(d_train,ii)[0]==i:
            c+=1
        else:
            print(k_nearest(d_train,ii)[1])
        t+=1
print(c/t)


































# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 12:03:26 2018

@author: prince khera
"""

import pandas as pd
import numpy as np
from sklearn import cross_validation, neighbors

df = pd.read_csv('breast_cancer.txt',names=['id','clump_thickness','unif_cell_size','unif_cell_shape','marg_adhesion','single_epith_cell_size', 'bare_nuclei','bland_chrom','norm_nucleioli','mitoses','class'])
df.replace('?',-99999,inplace=True)
df.drop(['id'],1,inplace=True)

X = np.array(df.drop(['class'],1))

y = np.array(df['class'])

X_train,X_test,y_train,y_test=cross_validation.train_test_split(X,y,test_size=.2)

clf = neighbors.KNeighborsClassifier()
clf.fit(X_train,y_train)

accuracy = clf.score(X_test,y_test)
t = np.array([[5,4,4,3,5,4,3,4,5]])
p = clf.predict(t)






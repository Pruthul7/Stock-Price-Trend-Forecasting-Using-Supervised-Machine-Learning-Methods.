# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 12:26:08 2020

@author: Pruthul
"""

import sys
import os
import csv
import pandas as pd
from sklearn.preprocessing import normalize


from sklearn.feature_selection import RFECV
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import StratifiedKFold
import numpy as np
def conv(s):
	try:
		s=float(s)
	except ValueError:
		pass    
	return s



	X = []
	y = []

	ranking = []



data = pd.read_csv('AAL.csv')



col = list(data.adj_close)

X = [ col[:2] ]
y = [ col[-1], col[-2] ]
print X
print y	

X=np.array(X, np.float64)
y=np.array(y, np.float64)

estimator = LinearRegression()
selector = RFECV(estimator, step=1, cv=StratifiedKFold(y, 2))
		
selector = selector.fit(X, y)
		
		
X = []
y = []

if len(ranking)!=0:
			ranking = [sum(x) for x in zip(ranking, selector.ranking_)]
else:
			ranking = selector.ranking_

print (ranking)

		


if __name__ == '__main__':
	main(sys.argv[1])
cols = data['high', 'open', 'low', 'close', 'volume', 'adj_close']

file_dataframe = normalize(data, cols)

    

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
data = pd.read_csv('AAL.csv')
columns = data.columns
print(columns)

adjclose = columns[-2]
print(adjclose)

s = pd.Series([1, 2, 3, 4])
s.rolling(2).mean()
dataframe[roll_n] = pd.rolling().mean(dataframe[returns], n)

    dataframe[roll_n] = dataframe[returns].rolling(n).mean()

    exp_ma = returns[7:] + "ExponentMovingAvg" + str(n)
    
    dataframe[exp_ma] = dataframe[returns].ewm( halflife=n).mean()
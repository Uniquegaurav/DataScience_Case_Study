#!/usr/bin/env python
# coding: utf-8

# In[24]:


#Question 2
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
df=pd.read_csv('Dataset/startup_funding.csv',encoding='utf-8')
df['InvestorsName'].dropna(inplace=True)
dict = {}
arr = df['InvestorsName']
for i in arr:
        if ',' not in i:
                dict[i] = dict.get(i,1) + 1
        else:
            string = i.strip().split(',')
            for j in string:
                    dict[j.strip()] = dict.get(j.strip(),1) + 1
dataf = pd.DataFrame(list(dict.values()),list(dict.keys()))
dataf = dataf.sort_values(by=[0],ascending = False)
l = dataf.index[:5]
count =dataf[0].values[:5]
plt.bar(l,count,width =0.6)
plt.xticks(rotation =40)
plt.show()
for i  in range(len(l)) :
    print(l[i],count[i])


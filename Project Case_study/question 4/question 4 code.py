#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Question 4
import csv
import pandas as pd
import numpy as np
df=pd.read_csv('Dataset/startup_funding.csv',encoding='utf-8')
df.dropna(subset = ['InvestorsName','StartupName'],inplace =True)
df.StartupName.replace('Flipkart.com','Flipkart',inplace =True)
df.StartupName.replace('Ola Cabs','Ola',inplace =True)
df.StartupName.replace('Olacabs','Ola',inplace =True)
df.StartupName.replace('Oyorooms','Oyo',inplace =True)
df['StartupName'].replace('OYO Rooms','Oyo',inplace=True)
df.StartupName.replace('Oyo Rooms','Oyo',inplace =True)
df.StartupName.replace('OyoRooms','Oyo',inplace =True)
df.StartupName.replace('Paytm Marketplace','Paytm',inplace =True)
df.InvestmentType.replace('PrivateEquity','Private Equity',inplace = True)
df.InvestmentType.replace('Crowd funding','Crowd Funding',inplace =True)
df.InvestmentType.replace('SeedFunding','Seed Funding',inplace =True)
df  = df[(df['InvestmentType']=='Crowdfunding')| (df['InvestmentType']=='Seed Funding')]
investors  =  []
startup = []
df.reset_index(drop =True)
for i in df.index:
        val = df.loc[i].InvestorsName
        st = df.loc[i].StartupName  
        if ',' not in val:
                investors.append(val)
                startup.append(st)
        else:
            string = val.strip().split(',')
            for j in string:
                    investors.append(j.strip())
                    startup.append(st)
data= list(zip(investors, startup)) 
dataf = pd.DataFrame(data,columns= ['INVESTORS','STARTUP'])
dataf = dataf.drop_duplicates()
investors = []
count = []
values = dataf.INVESTORS.value_counts()
for i in dataf.INVESTORS.value_counts().index[:8] :
    if i != ''and i != 'Undisclosed Investors'and i != 'Undisclosed investors':
        investors.append(i)
        count.append(values[i])
dataf.INVESTORS.value_counts()
for i in range(5) :
    print(investors[i],count[i])
explode = [0.01,0.02,0.03,0.04,0.05]
plt.pie(count,labels = investors,autopct ="%.2f%%",counterclock = False,startangle = 90,explode =explode)
plt.axis('equal')
plt.show()


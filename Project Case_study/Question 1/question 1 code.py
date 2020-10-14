#!/usr/bin/env python
# coding: utf-8

# In[2]:


# QUESTION 1
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
csv_data = pd.read_csv('Dataset/startup_funding.csv')
df =  csv_data.copy()
def change(city) :
    return  city.split('/')[0].strip()
df.dropna(subset= ["CityLocation"],inplace =True)
df.CityLocation = df.CityLocation.apply(change)
df.CityLocation.replace('bangalore','Bangalore',inplace =True)
df.CityLocation.replace('Delhi','New Delhi',inplace =True)
city_count = df.CityLocation.value_counts()
maxfunded_city = city_count.index[0]
count = city_count.values[0]
city_count
city = ['Bangalore','Mumbai','New Delhi','Gurgaon','Noida']
val = []
for i in city :
    val.append(city_count[i])
    print(i,city_count[i])
plt.bar(city,val)
plt.show()


# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 15:01:35 2020

@author: Nick
"""

import pandas as pd
import matplotlib.pyplot as plt

#%% Reading the csv and pulling appropriate columns

case = pd.read_csv(r'C:/Users/Nick/Desktop/Python Practice/TimeAge.csv')

agerange = case['age']
total = case['confirmed']
dead = case['deceased']

#%% Creating blank arrays to be appended (Looking for a more efficient way to do this)

test = []
cat = []
temp = []
temp1 = []
csums = []
dsums = []
pers = []
group = []

#%% Looping through and manipulating the data to make that sweet graph

for i in range(len(agerange)):
    test.append(int(agerange[i].replace('s','')))
    if (test[i] not in cat):
        cat.append(test[i])
        group.append(str(test[i]) + '-' + str(test[i] + 9))   
        
for i in range(len(cat)):
    for j in range(len(test)):
        if (cat[i]) == test[j]:
            temp.append(total[j])
            temp1.append(dead[j])
    csums.append(sum(temp))
    dsums.append(sum(temp1))
    pers.append((dsums[i]/csums[i]) * 100)
    
    del temp[:]        
    del temp1[:]
    
#%%  Plotting
      
plt.figure()    
plt.plot(group,csums,'.b', label = 'C Cases')
plt.plot(group,dsums,'.r', label = 'Deaths')
plt.title('Ligma Statistics')
plt.xlabel('Age Groups')
plt.ylabel('Cases')
plt.legend()
plt.grid('on')

plt.figure()    
plt.plot(group,pers,'.r', label = '% Dead')
plt.title('Ligma Percentages')
plt.xlabel('Age Groups')
plt.ylabel('% Death Rate')
plt.legend()
plt.grid('on')

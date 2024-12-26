# import the library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# Bar chart
'''
Bivariate Analysis
Numerical vs Categorical
Use case - Aggregate analysis of groups
'''


# simple bar chart
children = [10,20,40,10,30]
colors = ['red','blue','green','yellow','pink']

plt.bar(colors,children)
plt.bar(colors,children , color="black") # this will show the bars in black color



# horizontal bar chart
plt.barh(colors,children,color='black')


# to show it side by side
plt.bar(np.arange(df.shape[0]) - 0.2,df['2015'],width=0.2,color='yellow')
plt.bar(np.arange(df.shape[0]),df['2016'],width=0.2,color='red')
plt.bar(np.arange(df.shape[0]) + 0.2,df['2017'],width=0.2,color='blue')

plt.xticks(np.arange(df.shape[0]), df['batsman']) 
# xsticks will replace the numbers with the original names 
plt.show()


# if the name is bigger , and overlapping in x axis in the names 
plt.xticks(rotation='vertical')  # shows the names in vertical order





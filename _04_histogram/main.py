# import the library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


'''
Univariate Analysis
Numerical col
Use case - Frequency Count
'''

# simple data

data = [32,45,56,10,15,27,61]
plt.hist(data)
plt.hist(data,bins=[10,25,40,55,70])

# on some data
df = pd.read_csv('/content/vk.csv')

plt.hist(df['batsman_runs'],bins=[0,10,20,30,40,50,60,70,80,90,100,110,120])
plt.show()



# logarithmic scale
arr = np.load('/content/big-array.npy')
plt.hist(arr,bins=[10,20,30,40,50,60,70],log=True)
plt.show()
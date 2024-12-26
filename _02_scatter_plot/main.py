# import the library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Scatter plot
'''
Bivariate Analysis
numerical vs numerical
Use case - Finding correlation
'''

# plt.scatter simple function
x = np.linspace(-10,10,50)
y = 10*x + 3 + np.random.randint(0,300,50)
plt.scatter(x,y)


# size
tips = sns.load_dataset('tips')
# The below will show , if the size is more the tip size is more
plt.scatter(tips['total_bill'],tips['tip'],s=tips['size'])

plt.plot(tips['total_bill'],tips['tip'],'o')


# NOTE: sctter is slower  while plot is faster method

























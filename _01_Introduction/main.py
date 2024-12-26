# import the library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('default')

# Working with 2 colums is called Bivariate Analysis
# Working with more than 2 columns is called Multivariate Analysis

'''
Bivariate Analysis
categorical -> numerical and numerical -> numerical
Use case - Time series data
'''

# plotting a simple function
price = [48000,54000,57000,49000,47000,45000]
year = [2015,2016,2017,2018,2019,2020]

plt.plot(year,price)   # (x , y)


batsman = pd.read_csv('/content/sharma-kohli.csv')

# plotting a simple function
plt.plot(batsman['index'],batsman['V Kohli'])


# plotting multiple plots on single graph
plt.plot(batsman['index'],batsman['V Kohli'])
plt.plot(batsman['index'],batsman['RG Sharma'])


# labels
plt.title('Rohit Sharma Vs Virat Kohli Career Comparison')
plt.xlabel('Season')
plt.ylabel('Runs Scored')



# Styling
# coloring the graph
plt.plot(batsman['index'],batsman['V Kohli'],color='red')
plt.plot(batsman['index'],batsman['V Kohli'],color='#D9F10F')
plt.plot(batsman['index'],batsman['RG Sharma'],color='#FC00D6')

# line style and width
# solid  , dashed , dotted , dashdot
plt.plot(batsman['index'],batsman['V Kohli'],color='red',linestyle='solid',linewidth=2)
plt.plot(batsman['index'],batsman['RG Sharma'],color='blue',linestyle='dashdot',linewidth=2)
plt.plot(batsman['index'],batsman['V Kohli'],color='red',linestyle='--',linewidth=2)
plt.plot(batsman['index'],batsman['RG Sharma'],color='blue',linestyle='-.',linewidth=2)

# marker and marker_size
# D-> Diamond, o-> circle , +-> plus , s-> square , *-> star , x-> cross
plt.plot(batsman['index'],batsman['V Kohli'],color='#D9F10F',linestyle='solid',linewidth=3,marker='D',markersize=10)
plt.plot(batsman['index'],batsman['RG Sharma'],color='#FC00D6',linestyle='dashdot',linewidth=2,marker='o')



# legend
# legend -> location -> upper right, upper left, lower right, lower left
plt.plot(batsman['index'],batsman['V Kohli'],color='#D9F10F',linestyle='solid',linewidth=3,marker='D',markersize=10,label='Virat')
plt.plot(batsman['index'],batsman['RG Sharma'],color='#FC00D6',linestyle='dashdot',linewidth=2,marker='o',label='Rohit')

plt.legend(loc='upper right') # default behavior is left top
plt.legend(loc='best') # find the best location and place it 







# limiting axes
price = [48000,54000,57000,49000,47000,45000,4500000]
year = [2015,2016,2017,2018,2019,2020,2021]

plt.plot(year,price)
plt.ylim(0,75000) # want to see the change in price ranging from 0 to 75000 in y axis
plt.xlim(2017,2019) # want to see the change in price ranging from 2017 to 2019 in x axis


# grid
plt.grid()
plt.show()























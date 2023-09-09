import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error,mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split


data = pd.read_csv('pub.log.txt',sep=" ")
data.drop(axis = 1,columns = ['Unnamed: 8'],inplace = True)

data.rename(columns = {'2023-09-09':'Date'}, inplace = True)
data.rename(columns = {'03:26:26':'Time'}, inplace = True)
data.rename(columns = {'1.54':'CPU Usage'}, inplace = True)
data.rename(columns = {'16':'Logical CPUs Used'}, inplace = True)
data.rename(columns = {'65.5':'Virtual Memory (%)'}, inplace = True)
data.rename(columns = {'11':'Virtual Memory (GB)'}, inplace = True)
data.rename(columns = {'141.5':'Disk Usage'}, inplace = True)
data.rename(columns = {'192.168.56.1':'IP'}, inplace = True)
data.set_index(['Date'],inplace = True)
data.drop(axis = 1,columns=['Logical CPUs Used','IP'],inplace = True)
data.drop(axis = 1,columns=['Time'],inplace = True)
data.reset_index(drop = True)

x = data.drop('CPU Usage',axis = 1)
y = data['CPU Usage']
x_train, x_test, y_train, y_test = train_test_split(x,
                                                     y, test_size=0.25, random_state=365)


reg = LinearRegression()
reg.fit(x,y)
y_pred = reg.predict(x_test)

DTR = DecisionTreeRegressor(max_depth=30)
DTR.fit(x, y)

DTR_y = DTR.predict(x_test)

l = [65,10,103.8]

print(DTR.predict([l]))
print(reg.predict([l]))
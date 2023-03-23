# -*- coding: utf-8 -*-
"""House_PP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tvTMgzmQYsc3PE5WvSsCyGB74Qz0-8CU
"""

# Importing all necessary Libaries

import numpy as np # numpy used for mathematical operation on array
import pandas as pd  # pandas used for data manipulation on dataframe
import seaborn as sns # seaborn used for data visualization
import matplotlib.pyplot as plt # matplotlib used for data visualization
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

train = pd.read_csv("train.csv")


test = pd.read_csv("test.csv")


train.head(5)# prints the first five rows of the train dataset

test.head(5)# prints the first five rows of the test dataset

# Check for shape of both datasets 
print(train.shape)
print(   )
print(test.shape)

train.tail(5) # prints last five rows of a train dataset along with all columns 

test.tail(5) # prints last five rows of a test dataset along with all columns 

train.info()

test.info()

train.isna().sum()

test.isna().sum()

train.nunique()

test.nunique()

train[train.duplicated()] # it selects the duplicated values in train dataset

test[test.duplicated()] # it selects the duplicated values in test dataset

# Check for shape of both datasets after droping the duplicated values 
print(train.shape)
print(   )
print(test.shape)

# checking the correlation between the features of the train dataframe by ploting heatmap correlation
train_corr = train.corr() # finding the correlation of the each columns in the train dataframe, the correlation matrix to be visualized
plt.figure(figsize=(10,5)) # specify the width and height of the plot
trainplot = sns.heatmap(train_corr, annot=True,) # create a heatmap plot of a correlation matrix called "train_corr", with annotations displayed on the plot. "annot=True": enables the display of annotations on the heatmap, showing the correlation values for each pair of variables.
plt.title('Correlation plot') # giving the title to the plot 
plt.show() # display the figure

# checking the correlation between the features of the train dataframe by ploting heatmap correlation
test_corr = test.corr() # finding the correlation of the each columns in the train dataframe, the correlation matrix to be visualized
plt.figure(figsize=(10,5)) # specify the width and height of the plot
testplot = sns.heatmap(test_corr, annot=True,) # create a heatmap plot of a correlation matrix called "train_corr", with annotations displayed on the plot. "annot=True": enables the display of annotations on the heatmap, showing the correlation values for each pair of variables.
plt.title('Correlation plot') # giving the title to the plot 
plt.show() # display the figure

train.drop(['ADDRESS'], axis=1, inplace=True) # droping the address column 
test.drop(['ADDRESS'], axis=1, inplace=True) 

print(train.shape)
print(   )
print(test.shape)

train.dtypes

# converting categorical values to numerical values 
train = pd.get_dummies(data=train, columns=['POSTED_BY', 'BHK_OR_RK'], drop_first=True)
train.head()

train.dtypes

test.dtypes

test = pd.get_dummies(data=test, columns=['POSTED_BY', 'BHK_OR_RK'], drop_first=True)
test.head(5)

test.dtypes

print(train.shape)
print(   )
print(test.shape)

X = train.drop('TARGET(PRICE_IN_LACS)', axis=True)
X.head(5)

Y = train['TARGET(PRICE_IN_LACS)']
Y.head(5)

print(X.shape)
print(Y.shape)

test.shape

# splitting into x_train, y_train, x_test, y_test
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 42)

print(X_train.shape)
print(Y_train.shape)
print(X_test.shape)
print(Y_test.shape)

rfr = RandomForestRegressor()
rfr.fit(X_train, Y_train)

y_pred = rfr.predict(X_test)
y_pred

print('MAE:', mean_absolute_error(Y_test, y_pred))
print('MSE:', mean_squared_error(Y_test, y_pred))

y_test_pred=rfr.predict(test)
y_test_pred
  

import pickle # it will helps to pickling of the regression model, pickle file will stores the all the information regarding the model in a serialized format and then load the pickle file and do the prediction
# converting to pickle file 
pickle.dump(rfr, open('rfr.pkl','wb')) # rfr.pkl is file name which is created by open function and with write byte mode. 
# load the pickle file 
pickled_model=pickle.load(open('rfr.pkl','rb')) # rb = read byte mode
# prediction 
pickled_model.predict(X_test)




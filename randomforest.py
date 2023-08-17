import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt

#Reading csv from user

df = pd.read_csv("D:\S6\CloudLab\Iris.csv")

#defining input and target variables
x = df["PetalLengthCm"].values.reshape(-1,1)
y = df["SepalLengthCm"].values.reshape(-1,1)

#splitting the dataset 
x_train,x_test,y_train,y_test = train_test_split(x,y,random_state = 99,test_size = 0.5)

randomModel = RandomForestRegressor(random_state = 100)

randomModel.fit(x_train,y_train)

predicted_random = randomModel.predict(x_test)

plt.scatter(x_test,y_test, label = "Actual")
plt.scatter(x_test,predicted_random,label = "predicted")
plt.legend()
plt.show()



import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("Salary_Data.csv")
x = df["YearsExperience"].values.reshape(-1,1)
y = df["Salary"].values.reshape(-1,1)

train_x,test_x,train_y,test_y = train_test_split(x,y,test_size = 0.2,random_state=42)

regModel = LinearRegression()

regModel.fit(train_x,train_y)

predicted = regModel.predict(test_x)

mse = mean_squared_error(test_y,predicted)

user_years = np.array([float(input(f"Enter the value for year{i+1}") )for i in range(5)])
user_predicted = regModel.predict(user_years.reshape(-1,1))
print(user_predicted)
print(mse)
plt.plot(test_x,test_y,color = "red",marker = "*")
plt.scatter(test_x,predicted)
plt.show()
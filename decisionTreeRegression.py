import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor,plot_tree
from sklearn.model_selection import train_test_split

df = pd.read_csv("D:\S6\CloudLab\Iris.csv")

x = df["PetalLengthCm"].values.reshape(-1,1)
y = df["SepalLengthCm"].values.reshape(-1,1)

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state=99)

decision_tree = DecisionTreeRegressor()

decision_tree.fit(x_train,y_train)

predicted = decision_tree.predict(x_test)

plt.scatter(x_test,y_test,color = 'red',label = "Actual")
plt.scatter(x_test,predicted,color='blue',label = 'predicted')
plt.legend()
plt.show()
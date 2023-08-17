import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split

df = pd.read_csv("D:\S6\CloudLab\Iris.csv")

# Select multiple features and reshape them
X = df[["PetalLengthCm", "PetalWidthCm"]].values
y = df["SepalLengthCm"].values

# Reshape the features
X = X.reshape(-1, 2)

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=99)

decision_tree = DecisionTreeRegressor()
decision_tree.fit(x_train, y_train)
predicted = decision_tree.predict(x_test)

plt.scatter(x_test[:, 0], y_test, color='red', label="Actual")
plt.scatter(x_test[:, 0], predicted, color='blue', label='Predicted')
plt.legend()
plt.xlabel("Petal Length (cm)")
plt.ylabel("Sepal Length (cm)")
plt.title("Actual vs Predicted Sepal Length")
plt.show()

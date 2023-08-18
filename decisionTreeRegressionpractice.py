import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("D:/S6/CloudLab/Iris.csv")

# Separate features (X) and target variable (y) 
X = df["PetalLengthCm"].values.reshape(-1,1)
y = df["SepalLengthCm"].values.reshape(-1,1)

# Split the data into training and test sets
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.2, random_state=99)

# Initialize the DecisionTreeRegressor
model = DecisionTreeRegressor()

# Train the model
model.fit(train_X, train_y)

# Predict on the test set
predicted = model.predict(test_X)

# Calculate Mean Squared Error
mse = mean_squared_error(test_y, predicted)
print("Mean Squared Error:", mse)

# Visualize the decision tree
plt.figure(figsize=(12, 6))
plot_tree(model, filled=True)
plt.show()

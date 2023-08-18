import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder 
from sklearn.metrics import accuracy_score

data = pd.read_csv("Iris.csv")
x = data.drop('Species', axis=1)
y = data['Species']

encoder = LabelEncoder()
y = encoder.fit_transform(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

regressor = LogisticRegression()
regressor.fit(x_train, y_train)
predValue = regressor.predict(x_test)
accuracy = accuracy_score(predValue, y_test)

print("Accuracy:", accuracy)
print("Actual Values:", y_test)
print("Predicted Values:", predValue)
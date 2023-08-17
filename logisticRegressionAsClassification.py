import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

df = pd.read_csv("D:\S6\CloudLab\Housing.csv")
x = df.drop(['prefarea'],axis = 'columns')
y = df['prefarea']

#price,area,bedrooms,bathrooms,stories,mainroad,guestroom,basement,hotwaterheating,airconditioning,parking,prefarea,furnishingstatus

categorical_cols = ["price","area","bedrooms","bathrooms","stories","mainroad","guestroom","basement","hotwaterheating","airconditioning","parking","furnishingstatus"]

encoder = LabelEncoder()

for col in categorical_cols:
    x[col] = encoder.fit_transform(x[col])

x_train,x_test ,y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state = 42)

logmodel = LogisticRegression()

logmodel.fit(x_train,y_train)

y_pred = logmodel.predict(x_test)
accuracy = accuracy_score(y_test,y_pred)
print("Accuracy = ",accuracy)
print(y_test)
print(y_pred)
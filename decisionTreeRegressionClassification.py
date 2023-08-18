import pandas as pd
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
df = pd.read_csv("D:\S6\CloudLab\Iris.csv")
#Id,SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm,Species
x = df.drop(['Species'],axis = "columns")
y = df['Species']

encoder = LabelEncoder()

categorical_col = ["Id","SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm"]
for column in categorical_col:
    x[column] = encoder.fit_transform(x[column])

train_x,test_x,train_y,test_y = train_test_split(x,y,test_size = 0.2, random_state = 49)

decModel = DecisionTreeClassifier()

decModel.fit(train_x,train_y)

predicted = decModel.predict(test_x)

plt.figure(figsize = (18,9))
plot_tree(decModel,filled = True)
plt.show()

accuracy = accuracy_score(test_y,predicted)
print("Accuracy = ",accuracy)














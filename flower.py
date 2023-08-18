import pandas as pd

def largest():
    df = pd.read_csv("Iris.csv")
    df1 = df[df["Species"] == "Iris-setosa"]
    df2 = df[df["Species"] == "Iris-versicolor"]
    df3 = df[df["Species"] == "Iris-virginica"]
    df4 = df1.sort_values(by="PetalLengthCm",ascending = False)
    df5 = df2.sort_values(by="PetalLengthCm",ascending = False)
    df6 = df3.sort_values(by="PetalLengthCm",ascending = False)

    with open("largest.txt","w") as large:
        df4.head(3).to_csv(large,index = False)
        large.write("\n\n")
        df5.head(3).to_csv(large,index = False)
        large.write("\n\n")
        df6.head(3).to_csv(large,index = False)
        large.write("\n\n")

largest()
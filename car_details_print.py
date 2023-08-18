from threading import Thread
import pandas as pd
def write_petrol(type):
    df = pd.read_csv("D:\S6\CloudLab\car details v4.csv")
    if type == "Petrol":
        filtered_df = df[df["Fuel Type"] == "Petrol"]
        output = "petrol.txt"
        filtered_df.to_csv(output,sep = '\t')
    if type == "Diesel":
        filtered_df = df[df["Fuel Type"] == "Diesel"]
        output = "diesel.txt"
        filtered_df.to_csv(output,sep = '\t')

    if type == "CNG":
        filtered_df = df[df["Fuel Type"] == "CNG"]
        output = "cng.txt"
        filtered_df.to_csv(output,sep = ',')

def main():
    t1 = Thread(target = write_petrol,args = ("Petrol",))
    t2 = Thread(target = write_petrol,args = ("Diesel",))
    t3 = Thread(target = write_petrol,args = ("CNG",))       
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
if __name__ == "__main__":
    main()

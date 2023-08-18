import threading
from threading import Thread
r = int(input("Enter the number of rows"))
c = int(input("Enter the number of columns"))
matrix = []
print("Enter the matrix elements")

for i in range(r):
    a = []
    for j in range(c):
        a.append(int(input())) 
    matrix.append(a)

for i in range(r):
    for j in range(c):
        print(matrix[i][j],end = " ")
    print()    

min_value = float('inf')
max_value = float('-inf')
min_lock = threading.Lock() 
max_lock = threading.Lock() 

def min_pool(matrix):
    global min_value
    for i in range(0,r-1,2):
        for j in range(0,c-1,2):
            min_val = min(matrix[i][j],matrix[i][j+1],matrix[i+1][j],matrix[i+1][j+1])
            min_value = min(min_value,min_val)

def max_pool(matrix):
    global max_value
    for i in range(0,r-1,2):
        for j in range(0,c-1,2):
            max_val = max(matrix[i][j],matrix[i][j+1],matrix[i+1][j],matrix[i+1][j+1])
            max_value = max(max_value,max_val)
t1 = Thread(target=min_pool, args=(matrix,)) 
t2 = Thread(target=max_pool, args=(matrix,)) 
t1.start() 
t2.start() 
t1.join() 
t2.join() 
  
min_val_from_threads = min_value 
max_val_from_threads = max_value 
  
print("Min value from the threads:", min_val_from_threads) 
print("Max value from the threads:", max_val_from_threads)
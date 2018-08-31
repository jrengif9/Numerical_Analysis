import matplotlib.pyplot as plt
from numpy import *
import numpy as np 
import math
import xlsxwriter
import pandas as pd

plt.style.use('dark_background')
#fig.set_dpi(100)
#fig.add_subplot(1, 1, 1)

# INPUT

l = 10              # Endpont
t = 1               # Maximun Time
alpha = 2           # constant: 1/v  v:propagation speed
m = 10              # 
n = 20              #

# OUTPUT

h = 0.1
k = 0.05
lam = 1

def funf(num):
    return math.sin(math.pi * num)

def fung(num):
    return 0

matrix = np.zeros(shape=(m,n))

# Step 2

for j in range (1,n):
    matrix[0][j] = 0
    matrix[m-1][j] = 0


# Step 3
matrix[0][0] = funf(0)
matrix[m-1][0] = funf(l)

#print(funf(l))


# Step 4 - Initialize for t = 0 and t=k
for i in range(1,m-1):
    matrix[i][0] = funf(i*h)
    matrix[i][1] = ((1-lam**2) * funf(i*h)) + (((lam**2)/2) * (funf((i+1) *h) + funf(((i-1)*h)))) + (k * fung(i*h))

# Step 5 - Perform Matrix Multiplication
for j in range(1,n-1):
    for i in range(1,m-1):
        matrix[i][j+1] = (2*(1-lam**2) * matrix[i][j]) + ((lam**2) * (matrix[i+1][j] + matrix[i-1][j])) - matrix[i][j-1] 

# Step 6
for j in range(0,n):
    t = j*k
    for i in range(0,m):
        x = i*h

a = zeros(l+1)
xi = 0
for i in range(1,l+1):
    a[i] = h
    h += 0.1

b = zeros(l+1)
for i in range(1,l+1):
    b[i] = matrix[i-1][19]
print(a)
print(b)

df = pd.DataFrame (matrix)

## save to xlsx file

filepath = 'my_excel_file.xlsx'

df.to_excel(filepath, index=False)



plt.plot(a,b,'b')
plt.axis([0,1,-1,1])
plt.show()



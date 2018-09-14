
#First we have to import all the necessary modules and functions
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from numpy import *
import pandas as pd
import numpy as np


# INPUT. values that user have to enter manually
l = 1               # Endpont
t = 1               # Maximun Time
alpha = 2           # constant: 1/v  v:propagation speed
m = 10              # number of rows, 
n = 20              # number of columns

h = float(l)/float(m)
k = float(t)/float(n)
lam = (k*alpha)/h

#function f
def funf(num):
    return sin(pi * num)
    #return np.sin(np.pi * num)

#function g
def fung(num):
    return 0

#Create a matriz of m+1 rows and n+1 columns, cause it starst from zero
matrix = np.zeros(shape=(m+1,n+1))

# Step 2
for j in range (1,n+1):
    matrix[0][j] = 0
    matrix[m][j] = 0


# Step 3
matrix[0][0] = funf(0)
matrix[m][0] = funf(l)


# Step 4 - Initialize for t = 0 and t=k
for i in range(1,m):
    matrix[i][0] = funf(i*h)
    matrix[i][1] = (1-lam**2)*funf(i*h) + ((lam**2)/2)*(funf((i+1)*h) + funf((i-1)*h)) + (k*fung(i*h))


# Step 5 - Perform Matrix Multiplication
for j in range(1,n):
    for i in range(1,m):
        matrix[i][j+1] = 2*(1-lam**2)*matrix[i][j] + (lam**2)*(matrix[i+1][j]+matrix[i-1][j]) - matrix[i][j-1] 

# Step 6
for j in range(0,n+1):
    t = j*k
    for i in range(0,m+1):
        x = i*h

#save the array in an .xlsx file
df = pd.DataFrame (matrix)
filepath = 'my_excel_file.xlsx'
df.to_excel(filepath, index=False)

#we create a figure and its axis.
fig, ax = plt.subplots()
xdata = zeros(m+1)                 # Create an array of zeros of size  m+1
xi = 0
for i in range(0,m+1):
    xdata[i] =xi
    xi += h                        # the distance between one dot an another


ydata = zeros(m+1)                 # Create an array to the points in y axis
ln, = plt.plot([], [], 'r', animated=True)

def init():
	ax.set_xlim(0, 1)
	ax.set_ylim(-1.1, 1.1)
	ln.set_data(xdata,ydata)
	return ln,

def update(frame):
    for i in range(0,m+1):
        ydata[i] = matrix[i][frame]  # itearate trough the matrix to change the value for each frame
	ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, frames=n+1,
                    init_func=init, blit=True, interval = 150,repeat=False)
plt.show()	


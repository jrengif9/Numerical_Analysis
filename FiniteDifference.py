#First we have to import all the necessary modules and functions
import matplotlib.pyplot as plt
from scipy import *
from sympy import *
from matplotlib.animation import FuncAnimation
import pandas as pd
import numpy as np


print("WELCOME !!!")
print("Wave Equation Finite-Difference")
print("Software to approximate the solution to the wave equation")

print("Please enter the values requested below.")


x = Symbol("x")
# INPUT. values that user have to enter manually
f = input("Enter u(x,0): ")
g = input("Enter du/dy(x,0): ")
l = input("Enter endpoint: ")                    # Endpont
t = eval(input("Enter Maximum Time: "))                # Maximun Time
alpha = eval(input("Enter alpha constant: "))    # constant: 1/v  v:propagation speed
m = int(input("Enter m value: "))                # number of rows, 
n = int(input("Enter n value: "))                # number of columns


h = float(l)/float(m)
k = float(t)/float(n)
lam = (k*alpha)/h


def evalfun(fun,num):
    if "x" in str(fun):
        val = float(eval(str(fun.replace("x",str(num)))))
    else:   
        val = float(fun)

    return val


#Create a matriz of m+1 rows and n+1 columns, cause it starst from zero
matrix = np.zeros(shape=(m+1,n+1))

# Step 2
for j in range (1,n+1):
    matrix[0][j] = 0
    matrix[m][j] = 0


# Step 3
matrix[0][0] = evalfun(f,0)
matrix[m][0] = evalfun(f,l)


# Step 4 - Initialize for t = 0 and t=k
for i in range(1,m):
    matrix[i][0] = evalfun(f,i*h)
    matrix[i][1] = (1-lam**2)*evalfun(f,i*h) + ((lam**2)/2)*(evalfun(f,(i+1)*h) + evalfun(f,(i-1)*h)) + (k*evalfun(g,i*h))


# Step 5 - Perform Matrix Multiplication
for j in range(1,n):
    for i in range(1,m):
        matrix[i][j+1] = 2*(1-lam**2)*matrix[i][j] + (lam**2)*(matrix[i+1][j]+matrix[i-1][j]) - matrix[i][j-1] 

# Step 6
for j in range(0,n+1):
    t = j*k
    for i in range(0,m+1):
        x = i*h

excel_name = input("Enter the name you want for the .xlsx file:")

#save the array in an .xlsx file
df = pd.DataFrame (matrix)
filepath = excel_name + '.xlsx'
df.to_excel(filepath, index=False)


#we create a figure and its axis.
fig, ax = plt.subplots()
xdata = [0] * (m+1)                 # Create an array of zeros of size  m+1
xi = 0
for i in range(0,m+1):
    xdata[i] =xi
    xi += h                        # the distance between one dot an another


ydata = [0] * (m+1)                 # Create an array to the points in y axis
ln, = plt.plot([], [], 'r', animated=True)

yn = 0 - (float(1.5)) #+ 0.1)
yp = float(1.5) #+ 0.1

"""
for j in range(0,n+1):
    for i in range(0,m+1):
        ydata[i] = matrix[i][j]
    plt.plot(xdata, ydata, "r")

# naming the x axis 
plt.xlabel('x') 
# naming the y axis 
plt.ylabel('displacement') 
# giving a title to my graph 
plt.title('Wave Equation Finite-Difference') 
ax.set_ylim(yn, yp)
plt.show()



"""
def init():
    ax.set_xlim(0, float(l))
    ax.set_ylim(yn, yp)
    ln.set_data(xdata,ydata)
    return ln,

def update(frame):
    for i in range(0,m+1):
        ydata[i] = matrix[i][frame]  # itearate trough the matrix to change the value for each frame
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, frames=n+1,
                    init_func=init, blit=True, interval = 200,repeat=False)
plt.show()	

print("Finished program!!!")

print("\nDeveloped by:")
print("Brian F. Morales A.")
print("Jose A. Carvajal B.")
print("José O. Rengifo C.")
print("Nicolás Restrepo L.")
print("Nicholas Rose")



"""
\frac{\partial ^ 2 u}{\partial t ^ 2}-522^2 \frac{\partial ^ 2 u}{\partial x ^ 2}=0, \quad 0<x<1,\;0<t
"""
import matplotlib.pyplot as plt 
  
# line 1 points 
x1 = [1,2,3] 
y1 = [2,4,1] 
# plotting the line 1 points  
plt.plot(x1, y1, "r") 
  
# line 2 points 
x2 = [1,2,3] 
y2 = [4,1,3] 
# plotting the line 2 points  
plt.plot(x2, y2, "r") 
  
# naming the x axis 
plt.xlabel('x - axis') 
# naming the y axis 
plt.ylabel('y - axis') 
# giving a title to my graph 
plt.title('Two lines on same graph!') 
  

  
# function to show the plot 
plt.show()
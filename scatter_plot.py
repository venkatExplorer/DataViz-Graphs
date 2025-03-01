import numpy as np 
import matplotlib.pyplot as plt

a = [10,20,30,40,50,60,70,80]
b = [1,6,4,2,8,9,1,5]
x = [1,3,6,7,4,6,9,2]

plt.scatter(a,b, c = "green", s = 300, edgecolors='y', marker='o', alpha=0.5)
plt.scatter(a,x, c = "green", s = 400, edgecolors='r', marker='4', alpha=1)
plt.legend(['b','x'], loc = "best")
plt.title("Scatter Plot Demo")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.savefig("ScatterPlot.png") # to save the graph
plt.grid(True)

plt.show()
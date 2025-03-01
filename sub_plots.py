import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,10,1)
y = 2*x + 5 
z = 3*x + 10

plt.subplot(2,1,1)
plt.plot(x,y, marker = "o", color = "r")
plt.title("Graph1")

plt.subplot(2,1,2)
plt.plot(x,z, linestyle = "-", color = "b", marker = "D")
plt.title("Graph2")
plt.savefig("sub_plots.png")
plt.show()
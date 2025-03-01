import matplotlib.pyplot as plt
import numpy as np

x = np.arange(3,50,5)
y = 2*x + 5 

plt.plot(x,y, linewidth = "2.0", marker = "o", color = "r")
plt.title("Line Plot Demo")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.grid(True)
plt.savefig("lineplot.png")
plt.show()
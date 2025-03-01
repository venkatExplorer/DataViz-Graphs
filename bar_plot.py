import numpy as np 
import matplotlib.pyplot as plt

data = {"apples": 20, "mangos": 15, "lemon":30, "oranges": 10}
names = list(data.keys())
values = list(data.values())

plt.figure(figsize = (5,2))
plt.bar(names,values, color = "grey") # for horizontal bar replace plt.barh 
plt.title("Bar Graph")
plt.xlabel("Fruits")
plt.ylabel("Quantity")
plt.savefig("barplot.png") # to save the graph
plt.show()
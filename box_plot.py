import matplotlib.pyplot as plt

total = [20,4,5,0,6,45,64,6,23,65,77,88,99]
order = [10,54,32,12,35,65,78,6,55,44,1]
discount = [20,30,44,50,60,11,44,66,99,65,70]
data = list([total,order,discount])
plt.boxplot(data, showmeans = True)
plt.title("Box Plot Demo")
plt.grid(True)
plt.savefig("boxplot.png") # to save the graph
plt.show()

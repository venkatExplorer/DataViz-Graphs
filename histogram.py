import matplotlib.pyplot as plt 

numbers = [10,12,16,19,11,20,26,28,30,35,36,60,61,64,66,70,75,74,73,85,86,99,98]
plt.hist(numbers, bins = [0,20,40,60,80,100], edgecolor = "orange", color = "blue")
plt.title("Histogram Demo")
plt.xlabel("Range of values")
plt.ylabel("Frequency of values")
plt.grid(True)
plt.savefig("histogram.png")
plt.show()
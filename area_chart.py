import matplotlib.pyplot as plt 

x = range(1,15)
y = [1,4,6,8,5,7,6,3,7,8,3,9,2,6]

plt.stackplot(x,y, colors="black", alpha = 0.5)
plt.plot(x,y, color = "g")
plt.grid(True)
plt.title("Area Chat")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.savefig("AreaChat.png") # to save the graph
plt.show()

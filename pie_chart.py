import matplotlib.pyplot as plt

label = ["dog","cat","wolf","lion"]
sizes = [50,45,60,90]

plt.pie(sizes, labels = label, autopct = "%1.1f%%", shadow=True, startangle = 90)
plt.title("Pie Chart Demo")
plt.savefig("piechart.png")
plt.show()
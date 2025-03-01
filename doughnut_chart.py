import matplotlib.pyplot as plt

group_names = ["GroupA", "GroupB", "GroupC"]
group_size = [20,30,50]
size_centre = [5]
a,b,c = [plt.cm.Blues, plt.cm.Reds, plt.cm.Greens]
pie1 = plt.pie(group_size, labels = group_names, radius = 1.5, colors=[a(0.5),b(0.7),c(1.0)], labeldistance=1.1)
pie2 = plt.pie(size_centre, radius = 1.0, colors="w")
plt.savefig("doughtnut.png")
plt.show()
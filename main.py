import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style



X_data = np.random.random(50) * 100
Y_data = np.random.random(50) * 100

print(X_data)

plt.scatter(X_data, Y_data, c="#006020", s=90, marker="*", alpha=0.6)
plt.show()


years = [2006 + x for x in range(16)]
weights = [80, 83, 85, 86, 82, 81, 79, 83, 78,80, 82, 82, 83, 81, 80, 79]

plt.scatter(years, weights)
plt.show()

plt.scatter(years, weights, c='#006020', s=52, alpha=0.85)
plt.plot(years, weights,'b--' ,lw=3)
plt.show()


x = ['C++', 'C', 'Java', 'Python', 'JavaScript']
y = [20, 54, 27, 13, 67]

plt.bar(x, y, align='edge', width=0.6)
plt.show()

ages = np.random.normal(20, 1.5, 1000)

plt.hist(ages, bins=[ages.min(), 18, 21, ages.max()])
plt.hist(ages,bins=20,cumulative=True)
plt.show()


langs = ['C++', 'C', 'Java', 'Python', 'JavaScript']
votes = [50, 24, 19, 9, 38]
explodes = [0, 0, 0, 0.2, 0]

plt.pie(votes, labels=langs, explode = explodes, autopct="%.2f%%")
plt.show()

years= [2014 + x for x in range(8)]
income = [55, 62, 56, 61, 72, 72, 73,75]
income_ticks = list(range(50, 81, 2))

plt.plot(years, income)
plt.title("Income of Vinicin ( in USD)")
plt.xlabel("Year")
plt.ylabel("Yearly Income in USD")
plt.yticks(income_ticks, [f"${x}k" for x in income_ticks])

plt.show()


x1, y1 = np.random.random(100), np.random.random(100)
x2, y2 = np.arange(100), np.random.random(100)

plt.figure(1)
plt.scatter(x1, y1)

plt.figure(2)
plt.scatter(x2, y2)
plt.plot(x2, y2, c='#006020')

plt.show()


x = np.arange(100)

fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x, np.sin(x))
axs[0, 0].set_title("Sine Function")

axs[0, 1].plot(x, np.random.random(100))
axs[0, 1].set_title("Random Function")

axs[1, 0].plot(x, np.cos(x))
axs[1, 0].set_title("Cosine Function")

axs[1, 1].plot(x, np.log(x))
axs[1, 1].set_title("Log Function")

plt.suptitle("Four Graphs")
plt.tight_layout()
plt.show()

plt.savefig('fourgraphs.png', dpi=300, transparent=False, bbox_inches='tight')

ax = plt.axes(projection="3d")

x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) * np.cos(Y)


ax.plot_surface(X, Y, Z, cmap="Spectral")
ax.set_title("3D Project")
ax.set_xlabel("Test")
ax.view_init(azim=0, elev=90)
plt.show()
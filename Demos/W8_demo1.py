import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

#fig, axes = plt.subplots(3, 2)
fig = plt.figure()

ax1 = fig.add_subplot(3, 2, 3)
ax2 = fig.add_subplot(3, 2, 6)
ax1.set_xlabel("Random data x")
ax2.set_ylabel("No idea what's here")
ax1.set_xlim(1,3)

ax1.tick_params(which = "both", length = 20, color = "g")
ax2.tick_params(which = "major", length = 5)

ax2.xaxis.set_minor_locator(MultipleLocator(0.5))
ax1.xaxis.set_major_locator(MultipleLocator(1))

ax1.plot(x,y, "rx")
ax2.plot(x,y, "bo")

plt.show()
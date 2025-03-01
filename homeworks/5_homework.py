import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns


# TODO add ticks to plots

print('Задание 1')

# x = np.array([1, 5, 10, 15, 20])
# y1 = np.array([1, 7, 3, 5, 11])
# y2 = np.array([4, 3, 1, 8, 12])

# plt.plot(x, y1, '-ro', label='line 1')
# plt.plot(x, y2, '-.go', label='line 1')
# plt.legend()

# plt.show()


print('Задание 2')

# grid = plt.GridSpec(2, 2)
# ax = plt.subplot(grid[0, :])
# x = np.arange(1, 6)
# y = np.array([1, 7, 6, 3, 5])
# ax.plot(x, y)

# ax = plt.subplot(grid[1, 0])
# y = np.array([9, 4, 2, 4, 9])
# ax.plot(x, y)

# ax = plt.subplot(grid[1, 1])
# y = np.array([-7, -4, 2, -4, -7])
# ax.plot(x, y)

# plt.show()


print('Задание 3')

# x = np.arange(-5, 6)
# y = x ** 2
# plt.plot(x, y)
# plt.annotate('min', xy=(0, 0), xytext=(0, 10),
#              arrowprops=dict(facecolor='green'))

# plt.show()


print('Задание 4')

x = np.random.uniform(0, 7, 700)
y = np.random.normal(0, 7, 700)

fig, ax = plt.subplots()
bins = np.arange(0, 8, 1)
h = ax.hist2d(x, y, bins=[bins, bins], cmap='viridis', vmin=0, vmax=10)

ax.set_xlim(0, 7)
ax.set_ylim(0, 7)
ax.set_xticks(np.arange(0, 8, 1))
ax.set_yticks(np.arange(0, 8, 1))
fig.colorbar(h[3], ax=ax, shrink=0.5, anchor=(0, 0), aspect=5)

plt.show()

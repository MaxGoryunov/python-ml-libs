import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns


# TODO add ticks to plots

print('Задание 1')

x = np.array([1, 5, 10, 15, 20])
y1 = np.array([1, 7, 3, 5, 11])
y2 = np.array([4, 3, 1, 8, 12])

plt.plot(x, y1, '-ro', label='line 1')
plt.plot(x, y2, '-.go', label='line 1')
plt.legend()

plt.show()


print('Задание 2')

grid = plt.GridSpec(2, 2)
ax = plt.subplot(grid[0, :])
x = np.arange(1, 6)
y = np.array([1, 7, 6, 3, 5])
ax.plot(x, y)

ax = plt.subplot(grid[1, 0])
y = np.array([9, 4, 2, 4, 9])
ax.plot(x, y)

ax = plt.subplot(grid[1, 1])
y = np.array([-7, -4, 2, -4, -7])
ax.plot(x, y)

plt.show()

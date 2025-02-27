import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns


print('Задание 1')

x = np.array([1, 5, 10, 15, 20])
y1 = np.array([1, 7, 3, 5, 11])
y2 = np.array([4, 3, 1, 8, 12])

plt.plot(x, y1, '-ro', label='line 1')
plt.plot(x, y2, '-.go', label='line 1')
plt.legend()

plt.show()



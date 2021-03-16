import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 1, 0.01)
y = -x**2 + 2*x

plt.plot(x, y)
plt.show()
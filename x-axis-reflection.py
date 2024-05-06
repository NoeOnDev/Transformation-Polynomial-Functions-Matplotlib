import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.1, 2, 400)

y1 = -np.abs(np.log(x))
y2 = np.abs(np.log(x))

plt.figure()

plt.plot(x, y1, label='F(x) = -|Ln(x)|')
plt.plot(x, y2, label='F(x) = |Ln(x)|')

plt.legend()
plt.show()
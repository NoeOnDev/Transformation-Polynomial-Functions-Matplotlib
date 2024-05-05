# The graph of the function F(x) = x^2+2 is shown.

import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return x ** 2 + 2

x = np.linspace(-5, 5, 400)
y = func(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y, color='black')
plt.xlabel('', fontsize=14)
plt.ylabel('', fontsize=14)
plt.title('Gráfica de la función F(x) = x^2 + 2', fontsize=16)
plt.grid(True)

ax = plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_position('center')
ax.spines['top'].set_position('center')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.xlim(-5, 5)
plt.ylim(-5, 5)

x_ticks = np.arange(-5, 6, 1)
x_labels = [str(i) if i != 0 else '' for i in x_ticks]
y_ticks = np.arange(-5, 6, 1)
y_labels = [str(i) if i != 0 else '' for i in y_ticks]

plt.xticks(x_ticks, x_labels)
plt.yticks(y_ticks, y_labels)
plt.show()
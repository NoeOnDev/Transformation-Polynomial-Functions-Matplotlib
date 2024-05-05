# This script shows how to shift the x-axis to the left in a graph.
# The graph of the function F(x) = (x + 2)^2 is shown.

import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return (x + 2) ** 2

x = np.linspace(-10, 10, 400)
y = func(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y, color='black')
plt.xlabel('x', fontsize=14)
plt.ylabel('F(x)', fontsize=14)
plt.title('Gráfica de la función F(x) = (x+2)^2', fontsize=16)
plt.grid(True)
plt.axhline(y=0, color='k', linestyle='--')
plt.axvline(x=0, color='k', linestyle='--')

plt.xlim(-4, 4)
plt.xticks(np.arange(-4, 5, 1))
plt.ylim(0, 5)

plt.show()
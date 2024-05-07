import numpy as np
import matplotlib.pyplot as plt

def func_a(x):
    return abs(1 - x**2) + 3

x = np.linspace(-3, 3, 100)

y_a = [func_a(val) for val in x]

plt.figure(figsize=(8, 6))
plt.plot(x, y_a, linewidth=2, color='black')
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.title('Gráfica de la función f(x) = |1 - x^2| + 3', fontsize=16)
plt.grid(True)
plt.axhline(y=0, color='k', linestyle='--')
plt.axvline(x=0, color='k', linestyle='--')
plt.ylim(0, 10)
plt.yticks(np.arange(0, 11, 1))
plt.show()
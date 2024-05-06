import numpy as np
import matplotlib.pyplot as plt

def func1(x):
    return (x + 2) ** 2

def func2(x):
    return x ** 2

def func3(x):
    return (x - 2) ** 2

functions = [func1, func2, func3]
colors = ['red', 'blue', 'black']
labels = ['F(x) = (x+2)^2', 'F(x) = x^2', 'F(x) = (x-2)^2']

x_values = np.linspace(-10, 10, 400)

plt.figure(figsize=(8, 6))
for func, color, label in zip(functions, colors, labels):
    y_values = [func(x) for x in x_values]
    plt.plot(x_values, y_values, color=color, label=label)

plt.xlabel('x', fontsize=14)
plt.ylabel('F(x)', fontsize=14)
plt.title('Gráficas de las funciones', fontsize=16)
plt.grid(True)
plt.axhline(y=0, color='k', linestyle='--')
plt.axvline(x=0, color='k', linestyle='--')
plt.xlim(-4, 4)
plt.xticks(np.arange(-4, 5, 1))
plt.ylim(0, 5)
plt.legend()
plt.show()
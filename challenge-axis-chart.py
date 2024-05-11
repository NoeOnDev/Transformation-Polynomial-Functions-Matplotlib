import numpy as np
import matplotlib.pyplot as plt

def func1(x):
    return np.abs(x - 2) + 3

def func2(x):
    return x ** 2 + 2 * x

def func3(x):
    return np.sin(2 * x) + np.pi / 2

functions = [func1, func2, func3]
colors = ['red', 'blue', 'black']
labels = ['F(x) = |x - 2| + 3', 'F(x) = x^2 + 2x', 'F(x) = sen(2x) + π/2']

x_values = np.linspace(-10, 10, 400)

fig, axs = plt.subplots(3, figsize=(8, 12))

for ax, func, color, label in zip(axs, functions, colors, labels):
    y_values = [func(x) for x in x_values]
    ax.plot(x_values, y_values, color=color, label=label)
    ax.set_xlabel('x', fontsize=14)
    ax.set_ylabel('F(x)', fontsize=14)
    ax.set_title(label, fontsize=16)
    ax.grid(True)
    ax.axhline(y=0, color='k', linestyle='--')
    ax.axvline(x=0, color='k', linestyle='--')
    ax.set_xlim(-4, 4)
    ax.set_xticks(np.arange(-4, 5, 1))
    ax.set_ylim(-2, 10)
    ax.legend()

plt.tight_layout()
plt.show()
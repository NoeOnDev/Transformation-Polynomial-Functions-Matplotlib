import numpy as np
import matplotlib.pyplot as plt

def func1(x):
    return 0.5 * np.cos(x)

def func2(x):
    return np.cos(x)

def func3(x):
    return 2 * np.cos(x)

functions = [func1, func2, func3]
colors = ['red', 'blue', 'black']
labels = ['F(x) = 1/2 cos(x)', 'F(x) = cos(x)', 'F(x) = 2 cos(x)']

x_values = np.linspace(-2*np.pi, 2*np.pi, 400)

fig, axs = plt.subplots(3, figsize=(8, 12))

for ax, func, color, label in zip(axs, functions, colors, labels):
    y_values = func(x_values)
    ax.plot(x_values, y_values, color=color, label=label)
    ax.set_xlabel('x', fontsize=14)
    ax.set_ylabel('F(x)', fontsize=14)
    ax.set_title(label, fontsize=16)
    ax.grid(True)
    ax.axhline(y=0, color='k', linestyle='--')
    ax.axvline(x=0, color='k', linestyle='--')
    ax.set_xlim(-2*np.pi, 2*np.pi)
    ax.set_xticks(np.arange(-2*np.pi, 2.5*np.pi, 0.5*np.pi))
    ax.set_ylim(-2.5, 2.5)
    ax.legend()

plt.tight_layout()
plt.show()
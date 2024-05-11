import numpy as np
import matplotlib.pyplot as plt

def func1(x):
    return np.cos(0.5 * x)

def func2(x):
    return np.cos(x)

def func3(x):
    return np.cos(2 * x)

functions = [func1, func2, func3]
colors = ['red', 'blue', 'black']
labels = ['F(x) = cos(1/2 x)', 'F(x) = cos(x)', 'F(x) = cos(2x)']

x_values = np.linspace(-2*np.pi, 2*np.pi, 400)

fig, axs = plt.subplots(1, 3, figsize=(18, 6))

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
    ax.set_ylim(-1.5, 1.5)
    ax.legend()

plt.tight_layout()
plt.show()
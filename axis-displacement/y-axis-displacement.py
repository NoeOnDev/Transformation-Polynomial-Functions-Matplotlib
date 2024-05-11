import numpy as np
import matplotlib.pyplot as plt

def func1(x):
    return x ** 2 + 2

def func2(x):
    return x ** 2

def func3(x):
    return x ** 2 - 2

functions = [func1, func2, func3]
colors = ['red', 'blue', 'black']
labels = ['F(x) = x^2 + 2', 'F(x) = x^2', 'F(x) = x^2 - 2']

x = np.linspace(-5, 5, 400)

fig, axs = plt.subplots(1, 3, figsize=(18, 6))  # Modificado aquí

for ax, func, color, label in zip(axs, functions, colors, labels):
    y = func(x)
    ax.plot(x, y, color=color, label=label)
    ax.set_xlabel('', fontsize=14)
    ax.set_ylabel('', fontsize=14)
    ax.set_title('Gráficas de las funciones', fontsize=16)
    ax.grid(True)

    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)

    x_ticks = np.arange(-5, 6, 1)
    x_labels = [str(i) if i != 0 else '' for i in x_ticks]
    y_ticks = np.arange(-5, 6, 1)
    y_labels = [str(i) if i != 0 else '' for i in y_ticks]

    ax.set_xticks(x_ticks)
    ax.set_xticklabels(x_labels)
    ax.set_yticks(y_ticks)
    ax.set_yticklabels(y_labels)
    ax.legend()

plt.tight_layout()
plt.show()
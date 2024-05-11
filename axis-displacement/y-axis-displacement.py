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

plt.figure(figsize=(8, 6))

for func, color, label in zip(functions, colors, labels):
    y = func(x)
    plt.plot(x, y, color=color, label=label)

plt.xlabel('', fontsize=14)
plt.ylabel('', fontsize=14)
plt.title('Gráficas de las funciones', fontsize=16)
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
plt.legend()
plt.show()
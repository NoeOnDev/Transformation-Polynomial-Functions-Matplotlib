import numpy as np
import matplotlib.pyplot as plt

def square(x):
    """
    Returns the square of the input value.
    
    Parameters:
        x (float): The input value.

    Returns:
        float: The square of the input value.
    """
    return x ** 2

def square_plus_two(x):
    """
    Returns the square of the input value plus two.
    
    Parameters:
        x (float): The input value.

    Returns:
        float: The square of the input value plus two.
    """
    return x ** 2 + 2

def square_minus_two(x):
    """
    Returns the square of the input value minus two.
    
    Parameters:
        x (float): The input value.

    Returns:
        float: The square of the input value minus two.
    """
    return x ** 2 - 2

MIN_VALUE = -5
MAX_VALUE = 5

x_values = np.linspace(MIN_VALUE, MAX_VALUE, 400)

plt.figure(figsize=(8, 6))

colors = ['red', 'blue', 'black']
labels = ['F(x) = x^2 + 2', 'F(x) = x^2', 'F(x) = x^2 - 2']

for func, color, label in zip([square_plus_two, square, square_minus_two], colors, labels):
    y_values = [func(x) for x in x_values]
    plt.plot(x_values, y_values, color=color, label=label)

plt.xlabel('X', fontsize=14)
plt.ylabel('Y', fontsize=14)
plt.title('Gráficas de las funciones', fontsize=16)
plt.grid(True)

ax = plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_position('center')
ax.spines['top'].set_position('center')

plt.xlim(MIN_VALUE, MAX_VALUE)
plt.ylim(MIN_VALUE, MAX_VALUE)

x_ticks = np.arange(-5, 6, 1)
y_ticks = np.arange(-5, 6, 1)

plt.xticks(x_ticks, [str(i) if i != 0 else '' for i in x_ticks])
plt.yticks(y_ticks, [str(i) if i != 0 else '' for i in y_ticks])

plt.legend()
plt.show()
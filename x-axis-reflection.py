import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return -np.abs(np.log(x))

def f_abs(x):
    return np.abs(np.log(x))

x = np.linspace(0.01, 5, 400)

y = f(x)
y_abs = f_abs(x)

plt.figure(figsize=(6, 4))

plt.plot(x, y, label='$y = -| \ln(x) |$', color='b')
plt.plot(x, y_abs, label='$y = | \ln(x) |$', color='r')

plt.title('Gráficas de las funciones')
plt.legend()

plt.axhline(y=0, color='black', linestyle='-', linewidth=1)
plt.axvline(x=0, color='black', linestyle='-', linewidth=1) 

plt.gca().spines['left'].set_position(('data', 0))
plt.gca().spines['right'].set_color('none')
plt.gca().spines['bottom'].set_position(('data', 0))
plt.gca().spines['top'].set_color('none')

plt.grid(True)

plt.xlim([0, 5])
plt.ylim([-4, 4])

plt.tight_layout()

plt.show()
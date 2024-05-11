import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return -np.abs(np.log(x))

def f_abs(x):
    return np.abs(np.log(x))

x = np.linspace(0.01, 5, 400)

y = f(x)
y_abs = f_abs(x)

fig, axs = plt.subplots(1, 2, figsize=(12, 6))

axs[0].plot(x, y, label='$y = -| \ln(x) |$', color='b')
axs[1].plot(x, y_abs, label='$y = | \ln(x) |$', color='r')

for ax in axs:
    ax.set_title('Gráficas de las funciones')
    ax.legend()
    ax.axhline(y=0, color='black', linestyle='-', linewidth=1)
    ax.axvline(x=0, color='black', linestyle='-', linewidth=1) 
    ax.spines['left'].set_position(('data', 0))
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['top'].set_color('none')
    ax.grid(True)
    ax.set_xlim([0, 5])
    ax.set_ylim([-4, 4])

plt.tight_layout()
plt.show()
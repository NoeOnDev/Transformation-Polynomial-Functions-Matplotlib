import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi, 400)

y = np.sin(x)
y_abs = np.abs(np.sin(x))

plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(x, y, label='$F(x) = \sin(x)$', color='b')
plt.title('Gráfica de $F(x) = \sin(x)$')
plt.legend()
plt.axhline(y=0, color='black', linestyle='-', linewidth=1)
plt.axvline(x=0, color='black', linestyle='-', linewidth=1) 
plt.gca().spines['left'].set_position(('data', 0))
plt.gca().spines['right'].set_color('none')
plt.gca().spines['bottom'].set_position(('data', 0))
plt.gca().spines['top'].set_color('none')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(x, y_abs, label='$F(x) = |\sin(x)|$', color='r')
plt.title('Gráfica de $F(x) = |\sin(x)|$')
plt.legend()
plt.axhline(y=0, color='black', linestyle='-', linewidth=1)
plt.axvline(x=0, color='black', linestyle='-', linewidth=1) 
plt.gca().spines['left'].set_position(('data', 0))
plt.gca().spines['right'].set_color('none')
plt.gca().spines['bottom'].set_position(('data', 0))
plt.gca().spines['top'].set_color('none')
plt.grid(True)

plt.tight_layout()

plt.show()
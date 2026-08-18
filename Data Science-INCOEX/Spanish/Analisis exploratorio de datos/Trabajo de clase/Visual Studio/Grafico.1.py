import matplotlib.pyplot as plt
import numpy as np

# Datos
x = np.array([2, 4, 1, 6, 3, 5, 2])
y = np.array([45, 68, 30, 95, 52, 80, 40])
comercios = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# Puntos y etiquetas
plt.scatter(x, y, color='blue')
for i, txt in enumerate(comercios):
    plt.annotate(txt, (x[i] + 0.1, y[i]))

# Línea de tendencia (Regresión) y Correlación
m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x + b, color='red', label=f'r = {np.corrcoef(x, y)[0, 1]:.2f}')

# Formato
plt.title("Visitas vs. Monto del Pedido")
plt.xlabel("Visitas en el mes (X)")
plt.ylabel("Monto del pedido (Y)")
plt.grid(True)
plt.legend()

plt.show()
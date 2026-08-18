import numpy as np
import matplotlib.pyplot as plt

# Datos
gastos = [
    45, 52, 38, 60, 48,
    55, 42, 50, 58, 47,
    5, 53, 310, 44, 49
]

#gráfico de barras
plt.figure(figsize=(10, 5))
plt.bar(range(1, len(gastos) + 1), gastos, color='skyblue', edgecolor='black')


plt.title("Gráfico de Barras de Gastos", fontsize=14, fontweight='bold')
plt.xlabel("Registro / Transacción", fontsize=12)
plt.ylabel("Monto de Gastos", fontsize=12)
plt.xticks(range(1, len(gastos) + 1))
plt.grid(axis='y', linestyle='--', alpha=0.7)


plt.show()
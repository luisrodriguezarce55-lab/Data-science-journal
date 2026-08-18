import matplotlib.pyplot as plt

# Datos
gastos = [
    45, 52, 38, 60, 48,
    55, 42, 50, 58, 47,
    5, 53, 310, 44, 49
]

# Configuración de la gráfica
plt.figure(figsize=(6, 5))
plt.boxplot(
    gastos, 
    patch_artist=True,  # Permite rellenar con color
    boxprops=dict(facecolor='#a8dadc', color='#1d3557'),
    medianprops=dict(color='#e63946', linewidth=2),
    flierprops=dict(marker='o', markerfacecolor='#e63946', alpha=0.8)
)

# Títulos y etiquetas
plt.title("Distribución de Gastos", fontsize=14, fontweight='bold')
plt.ylabel("Monto de Gastos", fontsize=12)
plt.xticks([1], ['Gastos'])
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
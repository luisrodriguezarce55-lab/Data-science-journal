import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

# Datos
meses = list(range(1, 13))
tienda_fisica = [4200, 4150, 4300, 4180, 4250, 4100, 4220, 4190, 4260, 4150, 4300, 4230]
en_linea = [800, 870, 950, 1050, 1180, 1300, 1450, 1600, 1750, 1900, 2100, 2350]

# Cálculo de porcentajes
totales = [f + l for f, l in zip(tienda_fisica, en_linea)]
pct_fisica = [f / t * 100 for f, t in zip(tienda_fisica, totales)]
pct_linea = [l / t * 100 for l, t in zip(en_linea, totales)]

# Gráfica
plt.figure(figsize=(10, 5))
plt.plot(meses, pct_fisica, marker='o', label='% Tienda física')
plt.plot(meses, pct_linea, marker='s', label='% En línea')

# Configuración idéntica a la imagen
plt.title("Participación de Ventas por Canal")
plt.xlabel("Mes")
plt.ylabel("Porcentaje del Total")
plt.xticks(meses)
plt.ylim(0, 100)
plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter())
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt

# Datos
meses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
tienda_fisica = [4200, 4150, 4300, 4180, 4250, 4100, 4220, 4190, 4260, 4150, 4300, 4230]
en_linea = [800, 870, 950, 1050, 1180, 1300, 1450, 1600, 1750, 1900, 2100, 2350]

# Graficar
plt.plot(meses, tienda_fisica, label='Tienda física')
plt.plot(meses, en_linea, label='En línea')

# Detallar y mostrar
plt.title("Ventas Mensuales")
plt.xlabel("Mes")
plt.ylabel("Ventas (Miles de colones)")
plt.legend()
plt.show()
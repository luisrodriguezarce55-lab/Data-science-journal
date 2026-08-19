import matplotlib.pyplot as plt
import pandas as pd

# Recreación de los 50 datos para el boxplot basándonos en la tabla
# Mínimo=1, Q1=2, Mediana=3, Q3=4, Máximo=6, Atípico=14
datos_pedidos = (
    [1] * 5 + [2] * 10 + [3] * 15 + [4] * 10 + [5] * 5 + [6] * 4 + [14] * 1
)
df = pd.DataFrame(datos_pedidos, columns=["Dias_Entrega"])

# Variables del problema
q1 = 2
q3 = 4
ric = q3 - q1
lim_sup = q3 + 1.5 * ric
atipico = 14


print("=" * 65)
print(
    "Pregunta a) ¿Qué porcentaje de los pedidos se entregó en 4 días o menos?"
)
print("Respuesta: ●El porcentaje de pedidos que es de 75% debido Q3 es igual a 0.75 que eson los 4 dias .")
print("-" * 65)

print( 'RIC = Q_3 - Q_1 / RIC= 4 - 2 = 2')
print(
    "Pregunta b) ¿Cuál es el rango intercuartílico? ¿Qué representa en este contexto?"
)
print(
    f"Respuesta: RIC = {ric} días. Representa la variación del 50% central de los tiempos de entrega."
)
print("-" * 65)

print(
    "Pregunta c) El valor de 14 días, ¿por qué se considera atípico? Causa de negocio."
)

print( "LS = Q3 + 1.5*(RIC)   LS = 4 + 1.5(2) = 7 / LI = Q1 - 1.5*(RIC)   LI = 2 - 1.5(2) = -1")
print(
    f"Respuesta: Es atípico porque supera el límite superior de {lim_sup} días."
)
print(
    "Causa de negocio: Problemas de inventario, retrasos en aduana o fallas de logística."
)
print("=" * 65)

# Gráfico
plt.figure(figsize=(7, 3))
plt.boxplot(df["Dias_Entrega"], orientation="horizontal")
plt.title("Tiempo de Entrega de Pedidos (50 Pedidos - LMB)", fontweight="bold")
plt.xlabel("Tiempo de entrega (días)")

plt.tight_layout()
plt.show()
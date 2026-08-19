import matplotlib.pyplot as plt
import pandas as pd


datos = [18, 22, 25, 27, 29, 30, 31, 33, 35, 36, 38, 40, 42, 45, 98]
df = pd.DataFrame(datos, columns=["Monto"])


q1 = 27
q3 = 40
ric = q3 - q1
lim_inf = q1 - (1.5 * ric)
lim_sup = q3 + (1.5 * ric)
atipico = 98


print("=" * 60)
print("Pregunta a) Ordene los datos y calcule Q1 y Q3.")
print(" Mitad inferior es: 18, 22, 25, 27, 29, 30, 31 y la mediana es 27 /Q1= 27 /Mitad superior es : 35, 36, 38, 40, 42, 45, 98 y la mediana es 40 / Q3=40")
print(f"Respuesta: Q1 = {q1} y Q3 = {q3}")
print("-" * 60)

print("Pregunta b) Calcule el rango intercuartílico (RIC).")
print(" RIC = Q3 - Q1 /RIC = 40 - 27 = 13")
print(f"Respuesta: RIC = {ric}")
print("-" * 60)

print(
    "Pregunta c) Calcule los límites inferior y superior para detectar valores atípicos."
)
print(" Limite superior= Q3 +(1.5*RIC) = 40 +(1.5*13) = 59.5 / Limite inferior= Q1 - (1.5*RIC) 27 +(1.5*13) = 7.5")
print(f"Respuesta: Límite Inferior = {lim_inf} | Límite Superior = {lim_sup}")
print("-" * 60)

print(
    "Pregunta d) ¿Hay algún valor atípico en el conjunto de datos? Justifique su respuesta."
)
print(
    f"Respuesta: Sí, el valor {atipico} es atípico porque supera el límite superior ({lim_sup})."
)
print("=" * 60)

# Gráfico 
plt.figure(figsize=(7, 3))
plt.boxplot(df["Monto"], orientation="horizontal")
plt.title("Distribución de Pedidos")
plt.xlabel("Monto (miles de colones)")
plt.tight_layout()
plt.show()
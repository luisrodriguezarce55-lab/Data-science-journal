import matplotlib.pyplot as plt
import pandas as pd


datos_productos = {
    "Producto": ["Producto A", "Producto B"],
    "Media": [45000, 18000],
    "Desviacion_Estandar": [6750, 5400],
}
df = pd.DataFrame(datos_productos)


df["CV"] = (df["Desviacion_Estandar"] / df["Media"]) * 100

cv_a = df.loc[df["Producto"] == "Producto A", "CV"].values[0]
cv_b = df.loc[df["Producto"] == "Producto B", "CV"].values[0]


print("=" * 65)
print("Pregunta a")
print("Producto a /CV= (6750/45000)*100=15%/ Producto B /CV= (5400/18000)*100=30%")
print("Calcule el coeficiente de variación (CV) de cada producto.")
print(f"Respuesta: Producto A = {cv_a:.1f}% | Producto B = {cv_b:.1f}%")
print("-" * 65)

print(
    "Pregunta b) ¿Cuál producto tiene ventas relativamente más variables?"
    " Impacto en inventario."
)
print(
    f"Respuesta: El Producto B ({cv_b:.1f}% vs {cv_a:.1f}%). Exige mayor"
    "Las ventas con mayor porcentaje cv son menos predecible pero son mas relevantes para el stock porque aumenta sus ventas"
    " Entonces por la variabilidad ahi que tener un sistema de stock para mas controlado"
)
print("-" * 65)

print(
    "Pregunta c) Si hay asimetría positiva en el Producto A, ¿usar media o"
    " mediana?"
)
print(
    "Respuesta: ●Se utilizaria la mediana porque es el punto central de grafica o base de datos segun los datos obtenidos, y ademas representa mejor las ventas "
)
print("=" * 65)


plt.figure(figsize=(7, 4))
plt.bar(df["Producto"], df["CV"], color=["#4c72b0", "#dd8452"], width=0.5)
plt.title(
    "Comparación de Variabilidad Relativa (CV)", fontweight="bold"
)
plt.ylabel("Coeficiente de Variación (%)")
plt.ylim(0, 35)


for i, valor in enumerate(df["CV"]):
    plt.text(i, valor + 1, f"{valor:.1f}%", ha="center", fontweight="bold")

plt.tight_layout()
plt.show()
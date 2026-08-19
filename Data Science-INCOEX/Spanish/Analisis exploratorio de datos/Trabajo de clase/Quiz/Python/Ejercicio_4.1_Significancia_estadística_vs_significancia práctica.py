import matplotlib.pyplot as plt
import pandas as pd


datos_tiempos = {
    "Plataforma": ["Anterior", "Nueva"],
    "Tiempo_Promedio_Seg": [15.0, 14.6],  # Este se saco represantivo porque 0.4 es la diferencia
}
df = pd.DataFrame(datos_tiempos)

valor_p = 0.001
muestra_n = 8000


print("=" * 70)
print(f"a) ¿Es estadísticamente significativo? (p = {valor_p}):")
print(
    "Si p ≤ α  se rechaza H₀ .Como p = 0.001 < 0.05, se rechaza la hipótesis nula de que no hay diferencia entre las plataformas. El resultado es estadísticamente significativo."
)
print("-" * 70)

print("b) ¿Tiene relevancia práctica para el negocio?:")
print(
    " Probablemente no. 0.4 segundos es una diferencia mínima que, en la práctica, el usuario ni siquiera percibe. Para el negocio, esto no representa un cambio significativo en la experiencia del cliente ni en indicadores como conversión o satisfacción. Aquí se ve claro que significativo estadísticamente no es lo mismo que importante para el negocio"
)
print("-" * 70)

print(f"c) Papel del tamaño de la muestra (n = {muestra_n}):")
print("Un papel muy importante. Con muestras tan grandes 8 000 transacciones, incluso diferencias muy pequeñas y prácticamente irrelevantes pueden resultar estadísticamente significativas, porque el error estándar se reduce mucho al aumentar el tamaño de la muestra. Por eso el valor p tan bajo no necesariamente indica que el hallazgo sea importante en términos reales, sino que es un efecto del tamaño de la muestra")

print("=" * 70)


plt.figure(figsize=(6, 4))

plt.bar(
    df["Plataforma"],
    df["Tiempo_Promedio_Seg"],
    color=["#4c72b0", "#55a868"],
    width=0.4,
)
plt.title("Tiempo Promedio de Pago por Plataforma", fontweight="bold")
plt.ylabel("Tiempo (Segundos)")
plt.ylim(0, 18)


for i, tiempo in enumerate(df["Tiempo_Promedio_Seg"]):
    plt.text(i, tiempo + 0.3, f"{tiempo} s", ha="center", fontweight="bold")


plt.annotate(
    "Diferencia: -0.4s\n(p = 0.001)",
    xy=(0.5, 14.8),
    ha="center",
    fontweight="bold",
    color="#c44e52",
)

plt.tight_layout()
plt.show()
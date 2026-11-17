import matplotlib.pyplot as plt
import pandas as pd

# Creación del DataFrame con los datos del ejercicio
datos_casos = {
    "Caso": ["Caso A", "Caso B", "Caso C"],
    "Valor_p": [0.032, 0.184, 0.049],
    "Alpha": [0.05, 0.05, 0.01],
}
df = pd.DataFrame(datos_casos)

# Evaluación lógica de decisión
df["Rechaza_H0"] = df["Valor_p"] <= df["Alpha"]
df["Decisión"] = df["Rechaza_H0"].apply(
    lambda x: "Se rechaza H0" if x else "No se rechaza H0"
)


print("=" * 70)
print("Caso A (p = 0.032, α = 0.05):")
print(
    f"  Decisión: {df.loc[0, 'Decisión']}. "
    " Se rechaza H0, porque el valor p (0.032) es menor que (0.05), por lo que existe evidencia estadística suficiente a favor de la hipótesis alternativa."
)
print("-" * 70)

print("Caso B (p = 0.184, α = 0.05):")
print(
    f"  Decisión: {df.loc[1, 'Decisión']}. "
    "No se rechaza H0, porque el valor p (0.184) es menor que (0.05), realmente no existe ninguna informacion que anule la informacion."
)
print("-" * 70)

print("Caso C (p = 0.049, α = 0.01):")
print(
    f"  Decisión: {df.loc[2, 'Decisión']}. "
    "No se rechaza H0, porque el valor p (0.049) es menor que (0.05), no hay evidencia estadística suficiente para descartar la hipótesis nula."
)
print("=" * 70)

# Gráfico comparativo entre Valor p y Nivel de Significancia (Alpha)
plt.figure(figsize=(8, 4.5))

posiciones = range(len(df))
ancho_barra = 0.35

plt.bar(
    [p - ancho_barra / 2 for p in posiciones],
    df["Valor_p"],
    width=ancho_barra,
    label="Valor p",
    color="#091720",
)
plt.bar(
    [p + ancho_barra / 2 for p in posiciones],
    df["Alpha"],
    width=ancho_barra,
    label="Nivel α (Alpha)",
    color="#8a6c6c",
    alpha=0.7,
)

plt.xticks(posiciones, df["Caso"])
plt.ylabel("Probabilidad")
plt.title(
    "Comparación de Valor p vs. Nivel de Significancia (α)", fontweight="bold"
)
plt.legend()

# Marcar sobre las barras si se rechaza o no H0
for i in posiciones:
    p_val = df.loc[i, "Valor_p"]
    dec = "Rechaza H0" if df.loc[i, "Rechaza_H0"] else "No Rechaza H0"
    plt.text(
        i,
        max(p_val, df.loc[i, "Alpha"]) + 0.008,
        dec,
        ha="center",
        fontweight="bold",
        fontsize=9,
    )

plt.ylim(0, 0.22)
plt.tight_layout()
plt.show()
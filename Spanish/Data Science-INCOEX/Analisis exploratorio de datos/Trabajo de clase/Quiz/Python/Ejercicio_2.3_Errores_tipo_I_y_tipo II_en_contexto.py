import matplotlib.pyplot as plt
import pandas as pd


datos_matriz = [
    ["Decisión Correcta\n(1 - α)", "ERROR TIPO I\n(Mayor costo)"],
    ["ERROR TIPO II\n(Oportunidad)", "Decisión Correcta\n(1 - β)"],
]


print("=" * 70)
print("a) Error Tipo I en LMB:")
print(
    "Falso positivo, es como invertir en un sistema que no funciona pero estas invirtiendo tiempo y dinero sin un beneficio real"
)
print("-" * 70)

print("b) Error Tipo II en LMB:")
print(
    "Falso negativo nuevo sistema no mejora el tiempo cuando en realidad sí es más rápido"
)
print("-" * 70)

print("c) Error más costoso:")
print(
    "  Me parece mas costoso el error tipo 1 porque es un software que da sensacion que tiene mejora pero genera una migracion que va gastar mas dinero en la mejora "
)
print("=" * 70)


fig, ax = plt.subplots(figsize=(8, 4.5))


valores_color = [[0, 2], [1, 0]]

cax = ax.imshow(valores_color, cmap="Blues", alpha=0.6)


ax.set_xticks([0, 1])
ax.set_yticks([0, 1])
ax.set_xticklabels(
    ["No rechazar H0\n(Conservar actual)", "Rechazar H0\n(Cambiar sistema)"],
    fontweight="bold",
)
ax.set_yticklabels(
    ["H0 es Verdadera\n(No mejora)", "H0 es Falsa\n(Sí mejora)"],
    fontweight="bold",
)

ax.set_xlabel("La desicion", fontweight="bold", labelpad=10)
ax.set_ylabel("Sistema actual", fontweight="bold", labelpad=10)
ax.set_title("Matriz de Decisiones y Errores de Hipótesis (LMB)", fontweight="bold")


for i in range(2):
    for j in range(2):
        ax.text(
            j,
            i,
            datos_matriz[i][j],
            ha="center",
            va="center",
            fontsize=10,
            fontweight="bold",
            color="green",
        )

plt.tight_layout()
plt.show()
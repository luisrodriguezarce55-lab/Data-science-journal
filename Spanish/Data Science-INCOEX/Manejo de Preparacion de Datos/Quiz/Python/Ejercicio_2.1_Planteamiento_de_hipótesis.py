import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


datos_hipotesis = {
    "Caso": [
        "a) Tiempo respuesta",
        "b) Peso producto",
        "c) Política descuento",
    ],
    "H0 (Notación)": ["μ <= 24", "μ = 500", "μ <= μ0"],
    "H1 (Notación)": ["μ > 24", "μ != 500", "μ > μ0"],
    "Tipo de Prueba": [
        "Una cola (Derecha)",
        "Dos colas",
        "Una cola (Derecha)",
    ],
}
df_hipotesis = pd.DataFrame(datos_hipotesis)

print("=" * 70)
print(
    "a) LMB afirma que el tiempo promedio de respuesta al cliente es de 24h."
)
print("   H0: μ <= 24  ")
print("   H1: μ > 24  ")
print("-" * 70)

print(
    "b) El gerente quiere verificar si el peso promedio es de 500g."
)
print("   H0: μ = 500 ")
print("   H1: μ != 500 ")
print("-" * 70)

print("c) Se quiere comprobar si la política aumentó el monto promedio.")
print("   H0: μ1 <= μ0 ")
print("   H1: μ1 > μ0 ")
print("=" * 70)

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
x = np.linspace(-4, 4, 1000)
y = (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x**2)


axes[0].plot(x, y, color="black", lw=1.5)
axes[0].fill_between(x, y, where=(x >= 1.645), color="red", alpha=0.5, label="Región de Rechazo (H1)")
axes[0].axvline(1.645, color="red", linestyle="--")
axes[0].set_title("Prueba de Una Cola a la Derecha (Casos a y c)", fontweight="bold")
axes[0].set_yticks([])
axes[0].legend()


axes[1].plot(x, y, color="black", lw=1.5)
axes[1].fill_between(x, y, where=(x >= 1.96), color="red", alpha=0.5, label="Región de Rechazo (H1)")
axes[1].fill_between(x, y, where=(x <= -1.96), color="red", alpha=0.5)
axes[1].axvline(1.96, color="red", linestyle="--")
axes[1].axvline(-1.96, color="red", linestyle="--")
axes[1].set_title("Prueba de Dos Colas (Caso b)", fontweight="bold")
axes[1].set_yticks([])
axes[1].legend()

plt.tight_layout()
plt.show()
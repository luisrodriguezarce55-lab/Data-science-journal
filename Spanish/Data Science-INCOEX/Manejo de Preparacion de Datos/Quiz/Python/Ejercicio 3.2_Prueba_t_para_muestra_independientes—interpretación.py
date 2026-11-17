import matplotlib.pyplot as plt
import pandas as pd


datos_canales = {
    "Canal": ["Tienda Física", "Tienda en Línea"],
    "Media": [32500, 38900],
}
df = pd.DataFrame(datos_canales)

valor_p = 0.021
alpha = 0.05


print("=" * 70)
print("a) Planteamiento de Hipótesis:")
print("   H0: μ_física = μ_línea ")
print("   H1: μ_física != μ_línea ")
print("-" * 70)

print(f"b) Decisión Estadística (p = {valor_p}, α = {alpha}):")
print(f"   Decisión: Se rechaza H0 (ya que p = {valor_p} < α = {alpha}).")
print("-" * 70)

print("c) Conclusión de Negocio:")
print(
    "    los clientes de la tienda en línea gastan en promedio más dinero por transacción que los clientes de la tienda física."
)
print("=" * 70)


plt.figure(figsize=(6, 4))

plt.bar(df["Canal"], df["Media"], color=["#10c52b", "#201644"], width=0.4)
plt.title("Monto Promedio de Compra por Canal", fontweight="bold")
plt.ylabel("Monto Promedio (₡)")
plt.ylim(0, 48000)


for i, media in enumerate(df["Media"]):
    plt.text(i, media + 1000, f"₡{media:,.0f}", ha="center", fontweight="bold")

plt.tight_layout()
plt.show()
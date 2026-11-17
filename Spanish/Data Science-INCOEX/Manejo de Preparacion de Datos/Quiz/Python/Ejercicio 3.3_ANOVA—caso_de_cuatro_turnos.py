import matplotlib.pyplot as plt
import pandas as pd


datos_turnos = {
    "Turno": ["Mañana", "Tarde", "Noche", "Fin de semana"],
    "Promedio_Pedidos": [45, 42, 30, 38],
}
df = pd.DataFrame(datos_turnos)

valor_p = 0.007
alpha = 0.05


print("=" * 70)
print("a) Planteamiento de Hipótesis:")
print(
    "   H0:umañana=utarde=unoche=u fin de semana"
)
print("   H1: Al menos un turno tiene un promedio de pedidos diferente.H1=! u")
print("-" * 70)

print(f"b) Decisión Estadística (p = {valor_p}, α = {alpha}):")
print(f"   Decisión: Se rechaza H0 (ya que p = {valor_p} < α = {alpha}).")
print(
    "Se rechaza H0 porque 0.007 es menor y igual a 0.05 esto nos dice que el promedio de pedidos procesados por hora es diferente según el turno de trabajo."
)
print("-" * 70)

print("c) La conclusión del ANOVA, ¿indica cuál turno en particular es diferente de los demás? Explique qué se necesitaría para saberlo")
print(
    "En conclusion no se puede determinar el turno cual es diferente debido a que no a hay tanta informacion"
)
print("   exactamente qué par de turnos difieren entre sí.")
print("=" * 70)


plt.figure(figsize=(7, 4))

colores = ["#084853", "#55a868", "#F7070F", "#886ED8"]
plt.bar(
    df["Turno"],
    df["Promedio_Pedidos"],
    color=colores,
    width=0.45,
    edgecolor="black",
)

plt.title("Promedio de Pedidos Procesados por Hora según Turno", fontweight="bold")
plt.ylabel("Pedidos / Hora")
plt.ylim(0, 55)


for i, valor in enumerate(df["Promedio_Pedidos"]):
    plt.text(i, valor + 1.5, f"{valor}", ha="center", fontweight="bold")

plt.tight_layout()
plt.show()
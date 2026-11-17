import matplotlib.pyplot as plt
import pandas as pd


datos_soporte = {
    "Equipo": ["Equipo A", "Equipo B"],
    "n": [30, 32],
    "Tiempo_Promedio_Dias": [4.2, 3.1],
}
df = pd.DataFrame(datos_soporte)

valor_p = 0.006
alpha = 0.05


print("=" * 70)
print("Reporte - LMB")
print("=" * 70)
print('Los números muestran una brecha clara: el Equipo A tarda en promedio 4.2 días en cerrar una queja, mientras que el Equipo B lo hace en 3.1 días. Evaluando, el valor p obtenido 0.006 confirma que hubo un motivo porque sucedio esto.'
'Quitando los valores de lado el cliente tuvo una experiencia del cliente mejor con el equipo B. Vale la pena meterse a fondo en cómo trabaja el Equipo B, qué hace diferente, y ver si eso se puede llevar al Equipo A. Eso sí,'
'antes de sacar conclusiones apresuradas, hay que confirmar que cada parametro para confirmar que si son equipos que se le puede hacer una evaluacion igual')


plt.figure(figsize=(6, 4))

plt.bar(
    df["Equipo"],
    df["Tiempo_Promedio_Dias"],
    color=["#754244", "#3d5f45"],
    width=0.4,
)
plt.title("Tiempo Promedio de Resolución de Quejas", fontweight="bold")
plt.ylabel("Días por Queja")
plt.ylim(0, 5.5)


for i, dias in enumerate(df["Tiempo_Promedio_Dias"]):
    plt.text(i, dias + 0.15, f"{dias} días", ha="center", fontweight="bold")


plt.annotate(
    "Diferencia: -1.1 días\n(p = 0.006)",
    xy=(0.5, 3.8),
    ha="center",
    fontweight="bold",
    color="#4c72b0",
)

plt.tight_layout()
plt.show()
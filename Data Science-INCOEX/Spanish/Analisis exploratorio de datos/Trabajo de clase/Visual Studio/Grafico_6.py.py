import matplotlib.pyplot as plt
import pandas as pd

# Datos de rotación por trimestre y año
datos = {
    "Trimestre": ["Q1", "Q2", "Q3", "Q4"],
    "Año 1": [2.1, 2.4, 2.6, 3.2],
    "Año 2": [2.3, 2.6, 2.8, 3.5],
    "Año 3": [2.6, 2.9, 3.1, 3.9],
}

df = pd.DataFrame(datos)

# Configuración de la figura
plt.figure(figsize=(9, 6))

# 1. Graficar series de cada año
plt.plot(
    df["Trimestre"],
    df["Año 1"],
    marker="*",
    linewidth=2,
    label="Año 1",
    color="#0055d4",
)
plt.plot(
    df["Trimestre"],
    df["Año 2"],
    marker="*",
    linewidth=2,
    label="Año 2",
    color="#e68a00",
)
plt.plot(
    df["Trimestre"],
    df["Año 3"],
    marker="*",
    linewidth=2,
    label="Año 3",
    color="#009966",
)

# 2. Agregar líneas horizontales con tus valores calculados
## Linea rayada 1
plt.axhline(
    y=2.575,
    color="#0055d4",
    linestyle="--",
    alpha=0.7,
    label="Promedio A1 (2.575)",
)
## Linea rayada 2
plt.axhline(
    y=2.800,
    color="#e68a00",
    linestyle="--",
    alpha=0.7,
    label="Promedio A2 (2.8)",
)
## Linea rayada 3
plt.axhline(
    y=3.050,
    color="#009966",
    linestyle="--",
    alpha=0.7,
    label="Promedio A3 (3.05)",
)

# Estilos y formato

plt.title(
    " Trimestre de los años",
    fontsize=13,
    fontweight="bold",
)
plt.xlabel("Trimestre", fontsize=11)
plt.ylabel("Rotación de Inventario (veces)", fontsize=11)
plt.grid(True, linestyle="--", alpha=0.6)

# Leyenda fuera del área de trazado para mayor claridad
plt.legend(title="Año / Promedio", bbox_to_anchor=(1.02, 1), loc="upper left")

plt.tight_layout()
plt.show()
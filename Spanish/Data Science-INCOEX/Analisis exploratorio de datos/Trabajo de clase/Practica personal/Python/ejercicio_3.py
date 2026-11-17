# ==========================================
# PARTE 1: IMPORTACIÓN DE LIBRERÍAS
# ==========================================
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# ==========================================
# PARTE 2: ENTRADA DINÁMICA DE DATOS (INPUT PASO A PASO)
# ==========================================
print("=" * 60)
print("  EJERCICIO 3: TABLA DE FRECUENCIAS Y DISTRIBUCIÓN DE DATOS  ")
print("=" * 60)

total_clientes = int(input("¿Cuántos clientes deseas registrar?: "))

tiempos = []
for i in range(total_clientes):
    tiempo = float(
        input(f"Ingresa el tiempo de espera del cliente #{i + 1} (minutos): ")
    )
    tiempos.append(tiempo)

tiempos.sort()

amplitud = int(
    input("\nIngresa la amplitud para los intervalos (ejemplo: 3): ")
)

# Definición de límites [L_inf, L_sup) asegurando incluir el valor máximo
valor_min = int(min(tiempos))
valor_max = int(max(tiempos))
limites = list(range(valor_min, valor_max + amplitud + 1, amplitud))

# ==========================================
# PARTE 3: DETECCIÓN Y TRATAMIENTO DE DATOS ATÍPICOS (IQR)
# ==========================================
Q1 = np.percentile(tiempos, 25)
Q3 = np.percentile(tiempos, 75)
IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

atipicos = [x for x in tiempos if x < limite_inferior or x > limite_superior]

print("\n" + "=" * 60)
print("ANÁLISIS DE DATOS ATÍPICOS (OUTLIERS)")
print("=" * 60)

if atipicos:
    print(f"⚠️ Se detectaron los siguientes datos atípicos: {atipicos}")
    print(
        f"Límites IQR: Inferior = {limite_inferior:.2f} | Superior = {limite_superior:.2f}"
    )
    respuesta = (
        input("¿Deseas eliminarlos para el análisis? (s/n): ").strip().lower()
    )

    if respuesta == "s":
        datos_trabajo = [
            x for x in tiempos if limite_inferior <= x <= limite_superior
        ]
        print("✅ Datos atípicos eliminados correctamente.")
    else:
        datos_trabajo = tiempos.copy()
        print("ℹ️ Se mantuvieron los datos originales.")
else:
    datos_trabajo = tiempos.copy()
    print("✅ No se encontraron datos atípicos según el criterio IQR.")

# ==========================================
# PARTE 4: CONSTRUCCIÓN DE LA TABLA DE FRECUENCIAS
# ==========================================
intervalos = pd.cut(
    datos_trabajo, bins=limites, right=False, include_lowest=True
)
df_clases = (
    pd.DataFrame({"Tiempo": datos_trabajo, "Intervalo": intervalos})
    .groupby("Intervalo", observed=False)
    .size()
    .reset_index(name="Frecuencia Absoluta (f)")
)

total_n = len(datos_trabajo)
df_clases["Frecuencia Relativa (h)"] = (
    df_clases["Frecuencia Absoluta (f)"] / total_n
)
df_clases["Porcentaje (%)"] = df_clases["Frecuencia Relativa (h)"] * 100
df_clases["Frecuencia Acumulada (F)"] = df_clases[
    "Frecuencia Absoluta (f)"
].cumsum()

# Formato visual limpio para consola
df_tabla = df_clases.copy()
df_tabla["Intervalo"] = df_tabla["Intervalo"].astype(str)
df_tabla["Frecuencia Relativa (h)"] = df_tabla["Frecuencia Relativa (h)"].map(
    "{:.2f}".format
)
df_tabla["Porcentaje (%)"] = df_tabla["Porcentaje (%)"].map("{:.1f}%".format)

print("\n" + "=" * 60)
print("TABLA DE FRECUENCIAS AGRUPADAS")
print("=" * 60)
print(df_tabla.to_string(index=False))
print(f"Total de datos procesados (N): {total_n}")

# ==========================================
# PARTE 5: DESCRIPCIÓN DE LA FORMA DE LA DISTRIBUCIÓN
# ==========================================
media_aprox = np.mean(datos_trabajo)
mediana_aprox = np.median(datos_trabajo)

print("\n" + "=" * 60)
print("DESCRIPCIÓN DE LA DISTRIBUCIÓN (FORMA)")
print("=" * 60)
print(f"• Media: {media_aprox:.2f} min | Mediana: {mediana_aprox:.2f} min")

if media_aprox > mediana_aprox:
    print(
        "• La distribución presenta asimetría positiva (sesgada a la derecha),\n"
        "  lo que indica concentración de la mayoría de los clientes en tiempos de\n"
        "  espera bajos y pocos clientes experimentando tiempos de espera elevados."
    )
elif media_aprox < mediana_aprox:
    print(
        "• La distribución presenta asimetría negativa (sesgada a la izquierda)."
    )
else:
    print("• La distribución es simétrica.")

# ==========================================
# PARTE 6: SELECCIÓN Y GENERACIÓN DE GRÁFICOS VÁLIDOS
# ==========================================
print("\n" + "=" * 60)
print("MENÚ DE SELECCIÓN DE GRÁFICOS (DATOS CONTINUOS Y AGRUPADOS)")
print("=" * 60)
print("1. Histograma (Barras contiguas para representar intervalos)")
print("2. Polígono de Frecuencias (Línea de tendencias sobre marcas de clase)")

opcion = int(input("\nSelecciona el gráfico que deseas visualizar (1-2): "))

fig, ax = plt.subplots(figsize=(8, 5))

etiquetas = [
    f"[{limites[i]}-{limites[i+1]})" for i in range(len(limites) - 1)
]
frecuencias_abs = df_clases["Frecuencia Absoluta (f)"].tolist()

if opcion == 1:
    ax.bar(
        etiquetas,
        frecuencias_abs,
        width=1.0,
        color="#3498db",
        edgecolor="black",
        align="center",
    )
    ax.set_title("Histograma de Tiempos de Espera", fontweight="bold")
    ax.set_xlabel("Intervalos de Tiempo (minutos)")
    ax.set_ylabel("Frecuencia Absoluta (f)")

elif opcion == 2:
    marcas_clase = [
        (limites[i] + limites[i + 1]) / 2 for i in range(len(limites) - 1)
    ]
    ax.plot(
        marcas_clase, frecuencias_abs, marker="o", color="#e74c3c", linewidth=2
    )
    ax.set_title("Polígono de Frecuencias", fontweight="bold")
    ax.set_xlabel("Marca de Clase (Tiempo Medio del Intervalo)")
    ax.set_ylabel("Frecuencia Absoluta (f)")

else:
    print("\n⚠️ Opción no válida. Se requiere seleccionar 1 o 2.")

if opcion in [1, 2]:
    plt.tight_layout()
    plt.show()
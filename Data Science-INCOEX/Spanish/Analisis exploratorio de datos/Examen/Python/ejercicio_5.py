# ==========================================
# PARTE 1: IMPORTACIÓN DE LIBRERÍAS
# ==========================================
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# ==========================================
# PARTE 2: ENTRADA DINÁMICA DE DATOS
# ==========================================
print("=" * 60)
print("   EJERCICIO 5: COMPARATIVA DINÁMICA DE CAMPAÑAS DIGITALES   ")
print("=" * 60)

print("\n--- INGRESO DE DATOS PARA CAMPAÑA 1 ---")
nombre_1 = (
    input("Nombre de la campaña (ENTER para 'Campaña X'): ").strip()
    or "Campaña X"
)
clics_1 = float(
    input("Número de Clics (ENTER para 800): ").strip() or 800
)
conv_1 = float(
    input("Número de Conversiones (ENTER para 60): ").strip() or 60
)
ventas_1 = float(
    input("Ventas Totales ₡ (ENTER para 3600000): ").strip() or 3600000
)

print("\n--- INGRESO DE DATOS PARA CAMPAÑA 2 ---")
nombre_2 = (
    input("Nombre de la campaña (ENTER para 'Campaña Y'): ").strip()
    or "Campaña Y"
)
clics_2 = float(
    input("Número de Clics (ENTER para 500): ").strip() or 500
)
conv_2 = float(
    input("Número de Conversiones (ENTER para 45): ").strip() or 45
)
ventas_2 = float(
    input("Ventas Totales ₡ (ENTER para 2700000): ").strip() or 2700000
)

datos = {
    "Campaña": [nombre_1, nombre_2],
    "Clics": [clics_1, clics_2],
    "Conversiones": [conv_1, conv_2],
    "Ventas_Totales": [ventas_1, ventas_2],
}

# ==========================================
# PARTE 3: DETECCIÓN Y TRATAMIENTO DE DATOS ATÍPICOS (IQR)
# ==========================================
clics = datos["Clics"]
Q1 = np.percentile(clics, 25)
Q3 = np.percentile(clics, 75)
IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

atipicos = [x for x in clics if x < limite_inferior or x > limite_superior]

print("\n" + "=" * 60)
print("ANÁLISIS DE DATOS ATÍPICOS (OUTLIERS)")
print("=" * 60)

if atipicos:
    print(f"⚠️ Se detectaron datos atípicos en la métrica de clics: {atipicos}")
    respuesta = (
        input("¿Deseas eliminar las campañas atípicas? (s/n): ").strip().lower()
    )

    if respuesta == "s":
        indices = [
            i
            for i, x in enumerate(clics)
            if limite_inferior <= x <= limite_superior
        ]
        for clave in datos:
            datos[clave] = [datos[clave][i] for i in indices]
        print("✅ Datos atípicos eliminados.")
    else:
        print("ℹ️ Se mantuvieron todos los datos originales.")
else:
    print(
        "ℹ️ No se detectan valores atípicos (evaluación sobre 2 campañas)."
    )

df = pd.DataFrame(datos)

# ==========================================
# PARTE 4: CÁLCULOS ESTADÍSTICOS Y RECOMENDACIÓN
# ==========================================
df["Tasa de Conversión (%)"] = np.where(
    df["Clics"] > 0, (df["Conversiones"] / df["Clics"]) * 100, 0
)
df["Ticket Promedio (₡)"] = np.where(
    df["Conversiones"] > 0, df["Ventas_Totales"] / df["Conversiones"], 0
)

# Copia formateada para consola
df_mostrado = df.copy()
df_mostrado["Ventas_Totales"] = df_mostrado["Ventas_Totales"].map(
    "₡{:,.0f}".format
)
df_mostrado["Tasa de Conversión (%)"] = df_mostrado[
    "Tasa de Conversión (%)"
].map("{:.2f}%".format)
df_mostrado["Ticket Promedio (₡)"] = df_mostrado["Ticket Promedio (₡)"].map(
    "₡{:,.0f}".format
)

print("\n" + "=" * 60)
print("TABLA COMPARATIVA DE CAMPAÑAS DE MARKETING")
print("=" * 60)
print(df_mostrado.to_string(index=False))

# Evaluación cualitativa automática
c1_tasa, c2_tasa = (
    df.loc[0, "Tasa de Conversión (%)"],
    df.loc[1, "Tasa de Conversión (%)"],
)
c1_ticket, c2_ticket = (
    df.loc[0, "Ticket Promedio (₡)"],
    df.loc[1, "Ticket Promedio (₡)"],
)

eficiente = df.loc[0, "Campaña"] if c1_tasa > c2_tasa else df.loc[1, "Campaña"]

print("\n" + "=" * 60)
print("RECOMENDACIÓN DE NEGOCIO Y CONCLUSIÓN")
print("=" * 60)
print(
    f"• La **{eficiente}** es la más EFICIENTE capturando conversiones "
    f"({max(c1_tasa, c2_tasa):.2f}% vs {min(c1_tasa, c2_tasa):.2f}%).\n"
    f"• Ambos canales generan un Ticket Promedio de ₡{c1_ticket:,.0f} por venta.\n"
    f"• Recomendación: Reasignar presupuesto hacia **{eficiente}** por requerir "
    f"menos clics para concretar ventas, optimizando el costo por adquisición (CPA)."
)

# ==========================================
# PARTE 5: SELECCIÓN DE TIPO DE GRÁFICO
# ==========================================
print("\n" + "=" * 60)
print("MENÚ DE SELECCIÓN DE GRÁFICOS (COMPARATIVA)")
print("=" * 60)
print("1. Barras de Tasa de Conversión (%) (Eficiencia de conversión)")
print("2. Barras de Ticket Promedio (₡) (Monto promedio por transacción)")

opcion_input = input("\nSelecciona el tipo de gráfico (1-2): ").strip()
opcion = int(opcion_input) if opcion_input in ["1", "2"] else 1

fig, ax = plt.subplots(figsize=(8, 5))

if opcion == 1:
    barras = ax.bar(
        df["Campaña"],
        df["Tasa de Conversión (%)"],
        color=["#3498db", "#2ecc71"],
        width=0.4,
    )
    ax.bar_label(barras, fmt="%.2f%%", padding=3)
    ax.set_title(
        "Comparación de Eficiencia: Tasa de Conversión (%)", fontweight="bold"
    )
    ax.set_ylabel("Tasa de Conversión (%)")
    ax.set_ylim(0, max(df["Tasa de Conversión (%)"]) * 1.2)

elif opcion == 2:
    barras = ax.bar(
        df["Campaña"],
        df["Ticket Promedio (₡)"],
        color=["#e74c3c", "#9b59b6"],
        width=0.4,
    )
    ax.bar_label(barras, fmt="₡{:,.0f}", padding=3)
    ax.set_title("Comparación de Valor: Ticket Promedio (₡)", fontweight="bold")
    ax.set_ylabel("Monto Promedio por Venta (₡)")
    ax.set_ylim(0, max(df["Ticket Promedio (₡)"]) * 1.2)

plt.tight_layout()
plt.show()
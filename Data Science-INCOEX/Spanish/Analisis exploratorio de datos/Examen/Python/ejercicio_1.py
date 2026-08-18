# ==========================================
# PARTE 1: IMPORTACIÓN DE LIBRERÍAS
# ==========================================
import matplotlib.pyplot as plt
import pandas as pd

# ==========================================
# PARTE 2: ENTRADA INTERACTIVA DE DATOS
# ==========================================
canales = []
frecuencias = []

print("--- REGISTRO DE DATOS ---")
num_canales = int(input("¿Cuántos canales deseas ingresar?: "))

for i in range(num_canales):
    nombre = input(f"\nNombre del canal #{i + 1}: ")
    cantidad = int(input(f"Cantidad de clientes para '{nombre}': "))
    canales.append(nombre)
    frecuencias.append(cantidad)

# ==========================================
# PARTE 3: CÁLCULOS ESTADÍSTICOS
# ==========================================
df = pd.DataFrame(
    {"Canal de pedido": canales, "Frecuencia Absoluta (f)": frecuencias}
)

total_clientes = df["Frecuencia Absoluta (f)"].sum()
df["Frecuencia Relativa (h)"] = df["Frecuencia Absoluta (f)"] / total_clientes
df["Porcentaje (%)"] = df["Frecuencia Relativa (h)"] * 100

# ==========================================
# PARTE 4: IMPRESIÓN DE TABLA EN CONSOLA
# ==========================================
print("\n" + "=" * 40)
print("TABLA DE FRECUENCIAS RESULTANTE")
print("=" * 40)
print(df.to_string(index=False))
print(f"Total de clientes analizados: {total_clientes}\n")

# ==========================================
# PARTE 5: SELECCIÓN DE TIPO DE GRÁFICO
# ==========================================
print("=" * 40)
print("MENÚ DE SELECCIÓN DE GRÁFICOS (CATEGÓRICOS)")
print("=" * 40)
print("1. Gráfico de Barras (Comparar volúmenes por canal)")
print("2. Gráfico de Pie / Pastel (Mostrar proporción porcentual)")

opcion = int(input("\nSelecciona el tipo de gráfico que deseas (1-2): "))

fig, ax = plt.subplots(figsize=(8, 5))

if opcion == 1:
    # 1. Barras (Ideal para variables categóricas)
    barras = ax.bar(
        df["Canal de pedido"], df["Frecuencia Absoluta (f)"], color="#3498db"
    )
    ax.bar_label(barras)
    ax.set_title("Cantidad de Clientes por Canal (Barras)", fontweight="bold")
    ax.set_ylabel("Clientes")

elif opcion == 2:
    # 2. Pie (Ideal para porcentajes sobre el total)
    ax.pie(
        df["Porcentaje (%)"],
        labels=df["Canal de pedido"],
        autopct="%1.1f%%",
        startangle=90,
    )
    ax.set_title(
        "Distribución Porcentual por Canal (Pie)", fontweight="bold"
    )

else:
    print("\n⚠️ Opción no válida. Debes seleccionar 1 o 2.")

if opcion in [1, 2]:
    plt.tight_layout()
    plt.show()
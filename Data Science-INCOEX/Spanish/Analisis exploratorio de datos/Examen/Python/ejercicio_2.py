import matplotlib.pyplot as plt
import pandas as pd

# ==========================================
# PARTE 1: ENTRADA DE DATOS (INPUT POR BUCLE)
# ==========================================
print("==========================================")
print("     REGISTRO DE TIEMPOS DE LLAMADA       ")
print("==========================================")

total_datos = int(input("¿Cuántas llamadas vas a ingresar?: "))

datos = []
for i in range(total_datos):
    tiempo = float(
        input(f"Ingresa la duración de la llamada #{i + 1} (minutos): ")
    )
    datos.append(tiempo)

# Crear DataFrame con Pandas
df = pd.DataFrame({"Duracion": datos})

# ==========================================
# PARTE 2: CÁLCULOS CON PANDAS
# ==========================================
media = df["Duracion"].mean()
mediana = df["Duracion"].median()
moda = df["Duracion"].mode().tolist()
rango = df["Duracion"].max() - df["Duracion"].min()
varianza = df["Duracion"].var(ddof=1)
desviacion = df["Duracion"].std(ddof=1)
cv = (desviacion / media) * 100

# ==========================================
# PARTE 3: DETECCIÓN SIMPLE DE ATÍPICOS (IQR)
# ==========================================
q1 = df["Duracion"].quantile(0.25)
q3 = df["Duracion"].quantile(0.75)
iqr = q3 - q1

limite_inf = q1 - 1.5 * iqr
limite_sup = q3 + 1.5 * iqr

atipicos = df[
    (df["Duracion"] < limite_inf) | (df["Duracion"] > limite_sup)
]["Duracion"].tolist()

# ==========================================
# PARTE 4: MOSTRAR RESULTADOS EN CONSOLA
# ==========================================
print("\n==========================================")
print("          RESULTADOS ESTADÍSTICOS         ")
print("==========================================")
print(f"• Media:                 {media:.2f} min")
print(f"• Mediana:               {mediana:.2f} min")
print(f"• Moda(s):               {moda} min")
print(f"• Rango:                 {rango:.2f} min")
print(f"• Varianza Muestral:     {varianza:.2f} min²")
print(f"• Desviación Estándar:   {desviacion:.2f} min")
print(f"• Coeficiente Variación: {cv:.2f} %")

if len(atipicos) > 0:
    print(f"\n⚠️ Valores atípicos detectados: {atipicos}")
else:
    print("\n✅ No hay valores atípicos.")

# ==========================================
# PARTE 5: INTERPRETACIÓN DE NEGOCIO
# ==========================================
print("\n==========================================")
print("        INTERPRETACIÓN DEL SERVICIO       ")
print("==========================================")
print(f"1. La llamada promedio dura {media:.2f} minutos.")
print(
    f"2. La mediana es {mediana:.2f} minutos (representa mejor la muestra si hay valores atípicos)."
)
print(f"3. La variabilidad del servicio es del {cv:.2f}% (Coeficiente de Variación).")

# ==========================================
# PARTE 6: GRÁFICO (HISTOGRAMA CON PANDAS)
# ==========================================
print("\nGenerando gráfico...")

plt.figure(figsize=(7, 4))
plt.hist(df["Duracion"], bins=5, color="skyblue", edgecolor="black")

plt.axvline(media, color="red", linestyle="--", label=f"Media ({media:.1f})")
plt.axvline(
    mediana, color="green", linestyle="-", label=f"Mediana ({mediana:.1f})"
)

plt.title("Duración de Llamadas de Soporte")
plt.xlabel("Minutos")
plt.ylabel("Cantidad de Llamadas")
plt.legend()
plt.tight_layout()
plt.show()
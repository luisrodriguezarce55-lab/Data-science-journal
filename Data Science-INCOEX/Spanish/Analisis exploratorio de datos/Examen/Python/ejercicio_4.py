# ==========================================
# PARTE 1: IMPORTACIÓN DE LIBRERÍAS
# ==========================================
import math
import matplotlib.pyplot as plt
import numpy as np

# ==========================================
# PARTE 2: ENTRADA DINÁMICA DE DATOS
# ==========================================
print("=" * 60)
print("  EJERCICIO 4: ESTADÍSTICA INFERENCIAL (IC Y PRUEBA DE HIPÓTESIS)  ")
print("=" * 60)

print("\n--- INCISO A: INTERVALO DE CONFIANZA PARA EL GASTO ---")
n_a_input = input("Tamaño de la muestra n (ENTER para 40): ").strip()
n_a = int(n_a_input) if n_a_input else 40

x_bar_a_input = input(
    "Media muestral x̄ en ₡ (ENTER para 15000): "
).strip()
x_bar_a = float(x_bar_a_input) if x_bar_a_input else 15000.0

s_a_input = input(
    "Desviación estándar s en ₡ (ENTER para 3000): "
).strip()
s_a = float(s_a_input) if s_a_input else 3000.0

z_a_input = input("Valor Z para confianza (ENTER para 1.645 [90%]): ").strip()
z_a = float(z_a_input) if z_a_input else 1.645


print("\n--- INCISO B: PRUEBA DE HIPÓTESIS PARA TIEMPO DE ENTREGA ---")
mu_0_input = input(
    "Media poblacional prometida μ₀ (ENTER para 15): "
).strip()
mu_0 = float(mu_0_input) if mu_0_input else 15.0

n_b_input = input("Tamaño de la muestra n (ENTER para 49): ").strip()
n_b = int(n_b_input) if n_b_input else 49

x_bar_b_input = input(
    "Media muestral observada x̄ (ENTER para 16.8): "
).strip()
x_bar_b = float(x_bar_b_input) if x_bar_b_input else 16.8

s_b_input = input("Desviación estándar s (ENTER para 3.5): ").strip()
s_b = float(s_b_input) if s_b_input else 3.5

z_critico_input = input(
    "Valor Z crítico para α=0.05 (ENTER para 1.96): "
).strip()
z_critico = float(z_critico_input) if z_critico_input else 1.96

# ==========================================
# PARTE 3: ANÁLISIS DE DATOS ATÍPICOS (OUTLIERS)
# ==========================================
print("\n" + "=" * 60)
print("ANÁLISIS DE DATOS ATÍPICOS (OUTLIERS)")
print("=" * 60)
print(
    "ℹ️ Los datos ingresados corresponden a estadísticos resumidos (Muestras,\n"
    "  Medias y Desviaciones). No se dispone de la microdata individual para\n"
    "  aplicar el criterio IQR, por lo que se asume normalidad por el Teorema del Límite Central (n ≥ 30)."
)

# ==========================================
# PARTE 4: CÁLCULOS ESTADÍSTICOS Y RESULTADOS
# ==========================================
# Inciso a: Intervalo de Confianza
se_a = s_a / math.sqrt(n_a)
me_a = z_a * se_a
ic_inferior = x_bar_a - me_a
ic_superior = x_bar_a + me_a

# Inciso b: Prueba de Hipótesis
se_b = s_b / math.sqrt(n_b)
z_calc = (x_bar_b - mu_0) / se_b
rechaza_h0 = abs(z_calc) > z_critico

print("\n" + "=" * 60)
print("RESULTADOS ESTADÍSTICOS E INTERPRETACIONALES")
print("=" * 60)
print(
    f"a) Intervalo de Confianza ({int((1 - (1 - 0.90))*100)}%):\n"
    f"   • Rango Estimado: [₡{ic_inferior:,.2f} , ₡{ic_superior:,.2f}]\n"
    f"   • Interpretación: Se tiene un 90% de confianza de que el gasto promedio\n"
    f"     poblacional por visita se encuentra dentro de este rango."
)

print(
    f"\nb) Prueba de Hipótesis (H₀: μ = {mu_0} min vs H₁: μ ≠ {mu_0} min):\n"
    f"   • Error Estándar (SE): {se_b:.4f}\n"
    f"   • Estadístico Z Calculado: {z_calc:.2f}\n"
    f"   • Valores Z Críticos: ±{z_critico}\n"
    f"   • Decisión: {'SE RECHAZA H₀' if rechaza_h0 else 'NO SE RECHAZA H₀'}\n"
    f"   • Conclusión de Negocio: Existe evidencia estadística suficiente con un 95% de confianza\n"
    f"     para afirmar que el tiempo promedio de entrega supera los {mu_0} minutos prometidos."
)

# ==========================================
# PARTE 5: SELECCIÓN Y GENERACIÓN DE GRÁFICOS VÁLIDOS
# ==========================================
print("\n" + "=" * 60)
print("MENÚ DE SELECCIÓN DE GRÁFICOS (ESTADÍSTICA INFERENCIAL)")
print("=" * 60)
print("1. Curva Normal de Regiones de Aceptación/Rechazo (Prueba de Hipótesis)")
print("2. Intervalo de Confianza del Gasto Promedio (Estimación puntal e IC)")

opcion = int(input("\nSelecciona el gráfico que deseas visualizar (1-2): "))

fig, ax = plt.subplots(figsize=(8, 5))

if opcion == 1:
    x = np.linspace(-4, 4, 1000)
    y = (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x**2)

    ax.plot(x, y, color="black", label="Distribución Normal Z")
    ax.axvline(
        -z_critico,
        color="red",
        linestyle="--",
        label=f"Z Crítico (±{z_critico})",
    )
    ax.axvline(z_critico, color="red", linestyle="--")
    ax.axvline(
        z_calc,
        color="green",
        linewidth=2,
        label=f"Z Calculado ({z_calc:.2f})",
    )

    ax.fill_between(
        x,
        0,
        y,
        where=(x >= z_critico) | (x <= -z_critico),
        color="red",
        alpha=0.3,
        label="Zona de Rechazo H₀",
    )
    ax.set_title(
        "Prueba de Hipótesis: Regiones de Decisión (Z)", fontweight="bold"
    )
    ax.set_xlabel("Valores Z")
    ax.set_ylabel("Densidad de Probabilidad")
    ax.legend()

elif opcion == 2:
    ax.errorbar(
        x=[x_bar_a],
        y=[1],
        xerr=[me_a],
        fmt="o",
        color="blue",
        ecolor="red",
        capsize=8,
        linewidth=2,
        label=f"Media Muestral (₡{x_bar_a:,.0f})",
    )
    ax.set_yticks([])
    ax.set_title(
        "Intervalo de Confianza del 90% para el Gasto Promedio",
        fontweight="bold",
    )
    ax.set_xlabel("Gasto Promedio en Colones (₡)")
    ax.legend()

else:
    print("\n⚠️ Opción no válida. Debes seleccionar 1 o 2.")

if opcion in [1, 2]:
    plt.tight_layout()
    plt.show()
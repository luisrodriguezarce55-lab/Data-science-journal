import matplotlib.pyplot as plt
import pandas as pd


datos_pruebas = {
    "Situación": [
        "a) Mismo grupo (Antes/Después)",
        "b) 2 Sucursales (Heredia vs Alajuela)",
        "c) 1 Muestra vs Valor histórico (₡35k)",
        "d) 5 Sucursales distintas",
    ],
    "Prueba Estadística": [
        "Prueba t pareada",
        "Prueba t independiente",
        "Prueba t de 1 muestra",
        "ANOVA de 1 factor",
    ],
    "Num_Grupos": ["1 grupo (2 mediciones)", "2 grupos independientes", "1 grupo vs Referencia", "5 grupos independientes"],
}
df = pd.DataFrame(datos_pruebas)


print("=" * 70)
print("a) Comparar el tiempo de atención de un mismo grupo de 25 empleados antes y después de un nuevo software")
print("Lo mejor que se puede hacer hacer misma prueba dos veces antes y despues a la misma poblacion, es prueba pareada")
print("-" * 70)

print("b) Comparar ventas entre sucursal Heredia y Alajuela:")
print("Puede ser una muestra independiente ")
print("-" * 70)

print("c) Verificar si el gasto promedio es igual al histórico de ₡35 000:")
print("Preuba t con una muestra de un solo grupo")
print("-" * 70)

print("d) Comparar el nivel de satisfacción entre 5 sucursales:")
print("ANOVA, cuando se evalua mas de dos promedios")
print("=" * 70)


plt.figure(figsize=(8, 4.5))

colores = ["#ca1aa4", "#645f77", "#c44e52", "#58183E"]
barras = plt.barh(df["Situación"], [1, 2, 1, 5], color=colores, height=0.55)

plt.xlabel("Número de Grupos / Condiciones Comparadas", fontweight="bold")
plt.title("Guía de Selección de Pruebas Estadísticas (LMB)", fontweight="bold")
plt.xlim(0, 6)


for barra, prueba in zip(barras, df["Prueba Estadística"]):
    ancho = barra.get_width()
    plt.text(
        ancho + 0.1,
        barra.get_y() + barra.get_height() / 2,
        f"  → {prueba}",
        va="center",
        fontweight="bold",
        fontsize=9,
    )

plt.gca().invert_yaxis() 
plt.tight_layout()
plt.show()
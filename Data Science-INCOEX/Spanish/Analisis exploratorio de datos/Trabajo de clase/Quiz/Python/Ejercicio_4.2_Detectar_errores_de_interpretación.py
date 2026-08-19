import matplotlib.pyplot as plt
import pandas as pd


analisis_errores = {
    "Concepto": ["Valor p = 0.09", "Aumento observado", "Conclusión futura"],
    "Interpretación Errónea": [
        "Demuestra que NO hay ningún efecto.",
        "Probará que el empaque causó el alza.",
        "Garantiza que otros cambios funcionarán.",
    ],
    "Interpretación Correcta": [
        "Evidencia insuficiente para confirmar efecto.",
        "Pudo ser por azar o factores externos.",
        "Requiere más datos y análisis riguroso.",
    ],
}
df = pd.DataFrame(analisis_errores)

valor_p = 0.09
alpha = 0.05


print("=" * 70)
print("a) Identificación de Errores en la Conclusión:")
print(
    "   1.  Dice que no rechazar H0 demuestra que no hay efecto, y eso está mal. No rechazar H0 no prueba nada, solo dice que con esos datos no hubo evidencia suficiente para rechazarla. Pero es probable que hay un efecto pero la muestra no alcanzó para detectarlo. Una cosa es no vimos evidencia y otra muy distinta es comprobamos que no existe.")
print("2Está confundiendo correlación con causalidad. Que las ventas subieran cuando cambiaron el empaque no significa que el empaque fue el culpable, pudo ser cualquier otra cosa que se entre enlaza. El texto se contradice dando mas relevancia al argumento: primero dice que el empaque no tuvo efecto, y en la misma frase lo usa como prueba de que sí funcionó.")
print("3Significa que cambios parecidos van a subir las ventas en el futuro, sin ninguna base. Eso es tirar conclusiones al aire con un solo caso.."
)
print(
    "   2. Asumir causalidad sin significancia y extrapolar a 'éxito futuro"
    " garantizado'."
)
print("-" * 70)

print(f"b) Conclusión Correcta y Honesta (p = {valor_p}, α = {alpha}):")
print(
    "Con un valor p de 0.09, que es mayor al 0.05 que usamos como referencia, no tenemos evidencia suficiente para decir que el empaque nuevo cambió las ventas. Pero ojo, eso tampoco quiere decir que no haya tenido ningún efecto, simplemente no lo pudimos comprobar con estos datos. El aumento en ventas que vimos pudo deberse al empaque, a otro factor que no estamos midiendo, o hasta variación normal. Antes de sacar conclusiones definitivas convendría tener más datos o controlar otras variables, y no deberíamos asumir que un cambio similar en el futuro va a repetir este resultado")


plt.figure(figsize=(6, 4))

plt.bar(
    ["Nivel de Significancia (α)", "Valor p Obtenido"],
    [alpha, valor_p],
    color=["#471b2e", "#c44e52"],
    width=0.4,
)
plt.axhline(
    y=alpha, color="black", linestyle="--", alpha=0.7, label="Umbral α = 0.05"
)

plt.title("Comparación de Valor p vs. Decisiones", fontweight="bold")
plt.ylabel("Probabilidad")
plt.ylim(0, 0.12)


plt.text(0, alpha + 0.005, f"α = {alpha}", ha="center", fontweight="bold")
plt.text(1, valor_p + 0.005, f"p = {valor_p}\n(No Significativo)", ha="center", fontweight="bold")

plt.tight_layout()
plt.show()
import numpy as np
import scipy.stats as stats  

########## EJERCICIO 1 ###############
print("#####################################")
print("EJERCICIO 1")
print("#####################################")
print("H₀ (hipótesis nula): μ = 500 ml")
print("H₁ (hipótesis alternativa): μ ≠ 500 ml (prueba de dos colas)")



# 1) Datos: volúmenes registrados de las botellas
pesos = np.array([498, 501, 499, 502, 500, 497, 503, 499, 501, 500])

# 2) Valor hipotético de la media bajo H0
mu0 = 500

# 3) Prueba t de una muestra
res = stats.ttest_1samp(pesos, mu0)

# 4) Extraer resultados
t_stat = res.statistic
p_value = res.pvalue

# 5) Nivel de significancia
alpha = 0.05

# 6) Resultados
print("t =", t_stat)
print("p-value =", p_value)

if p_value < alpha:
    print("Rechazo H0: hay evidencia de que la media es distinta de 500 ml.")
else: 
    print("No rechazo H0: no hay evidencia suficiente para decir que la media es diferente de 500 ml.")

#CONCLUSIONES
print("*************Conclusion*************************")
print("Con un nivel de significancia de 0.05,"
" no existe evidencia suficiente para afirmar " \
"que el contenido promedio de las botellas sea diferente de 500 ml. Por lo tanto, " \
"la afirmación de la empresa no puede ser rechazada.")

########## EJERCICIO 2 ###############
print("#####################################")
print("EJERCICIO 2")
print("#####################################")
print("H₀ (hipótesis nula): μ₁ = μ₂ (no hay diferencia en las calificaciones)")
print("H₁ (hipótesis alternativa): μ₁ ≠ μ₂ (sí hay diferencia en las calificaciones)")

# 1) Datos: grupos de estudiantes
Grupo_musica = np.array([65, 70, 68, 72, 66, 69, 71, 67, 70, 68])
Grupo_silencio = np.array([85, 88, 90, 87, 92, 86, 89, 91, 88, 90])

# 2) Prueba t para 2 muestras independientes (Welch)
res = stats.ttest_ind(Grupo_musica, Grupo_silencio, equal_var=False)

# 3) Extraer resultados
t_stat = res.statistic
p_value = res.pvalue

# 4) Nivel de significancia
alpha = 0.01

# 5) Resultados
print("t =", t_stat)
print("p-value =", p_value)

if p_value < alpha:
    print("Rechazo H0: hay evidencia de que existe una diferencia significativa entre los grupos.")
else: 
    print("No rechazo H0: no hay evidencia suficiente para afirmar que existe diferencia entre los grupos.")

# CONCLUSIÓN
print("************* Conclusion *************************")
print("Con un nivel de significancia de 0.01, existe evidencia estadísticamente significativa "
      "para afirmar que hay diferencia en las calificaciones entre los estudiantes que estudian "
      "con música y los que estudian en silencio.")



########## EJERCICIO 3 ###############
print("#####################################")
print("EJERCICIO 3")
print("#####################################")
print("H₀ (hipótesis nula): La distribución de estudiantes sigue las proporciones históricas (40%, 35%, 25%).")
print("H₁ (hipótesis alternativa): La distribución de estudiantes es diferente a las proporciones históricas.")

# 1) Frecuencias observadas
observadas = np.array([200, 120, 80])

# 2) Proporciones esperadas
p = np.array([0.40, 0.35, 0.25])

# 3) Total de estudiantes
n = observadas.sum()

# 4) Frecuencias esperadas
esperadas = n * p

# 5) Prueba chi-cuadrado
res = stats.chisquare(f_obs=observadas, f_exp=esperadas)

# 6) Resultados
chi2 = res.statistic
p_value = res.pvalue
gl = len(observadas) - 1

# 7) Mostrar resultados
print(f"Frecuencias Observadas: {observadas}")
print(f"Frecuencias Esperadas: {esperadas}")
print(f"Chi-cuadrado: {chi2:.4f}")
print(f"Grados de libertad: {gl}")
print(f"p-value: {p_value:.4f}")

# 8) Decisión
alpha = 0.05

if p_value < alpha:
    print("Rechazo H0: hay evidencia de que la distribución ha cambiado.")
else: 
    print("No rechazo H0: no hay evidencia suficiente para decir que la distribución es diferente.")

# CONCLUSIÓN
print("************* Conclusion *************************")
print("Con un nivel de significancia de 0.05, existe evidencia estadísticamente significativa "
      "para afirmar que la distribución de estudiantes por carrera ha cambiado respecto a las proporciones históricas.")

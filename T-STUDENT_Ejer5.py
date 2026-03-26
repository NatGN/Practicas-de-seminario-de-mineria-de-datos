# Ejercicio 5: 
# Una fábrica afirma que sus sacos de café pesan exactamente 500 gramos. 
# Un inspector de calidad sospecha que el peso es menor y toma una muestra de 15 sacos.
# Los pesos registrados son:
# [495, 498, 502, 490, 497, 499, 501, 493, 496, 498, 492, 495, 500, 494, 496]. 
# ¿Hay evidencia suficiente para decir que el peso promedio es diferente a 500 gramos con un α=0.05?

import numpy as np
from scipy import stats

#1) Datos: pesos registrados de los sacos de cafe
pesos = np.array([495, 498, 502, 490, 497, 499, 501, 493, 496, 498, 492, 495, 500, 494, 496])

#2) Valor hipotetico de la media bajo H0
mu0 = 500

#3) Ejecute la prueba t de 1 muestra
res = stats.ttest_1samp(pesos, mu0)

#4) Extrae el estadistico t y el p-value
t_stat = res.statistic
p_value = res.pvalue

#5) Define el nivel de significancia (alpha)
alpha = 0.05

#6) Decide si rechazas H0
print("t = ", t_stat)
print("p-value = ", p_value)

if p_value < alpha:
    print("Rechazo H0: hay evidencia de que la media es distinta de 500.")
else: 
    print("No rechazo H0: no hay evidencia suficiente para decir que la media es diferente")

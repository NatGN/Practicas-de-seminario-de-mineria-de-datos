# Ejercicio 6:
# Un analista quiere comparar el rendimiento (km/litro) de dos tipos de gasolina (A y B).
# Gasolina A: [12.5, 13.2, 12.8, 14.0, 13.5, 12.9, 13.1]
# Gasolina B: [14.2, 15.0, 14.8, 13.9, 15.5, 14.7, 15.1]
# ¿Existe una diferencia significativa en el rendimiento entre ambos tipos de gasolina?

import numpy as np
from scipy import stats

#1) Datos: rendimiento de las dos gasolinas
gasolina_A = np.array([12.5, 13.2, 12.8, 14.0, 13.5, 12.9, 13.1])
gasolina_B = np.array([14.2, 15.0, 14.8, 13.9, 15.5, 14.7, 15.1])

#2) Valor hipotetico de la diferencia bajo H0 (diferencia = 0)
# H0: media_A = media_B  →  media_A - media_B = 0

#3) Ejecute la prueba t para 2 muestras independientes
res = stats.ttest_ind(gasolina_A, gasolina_B)

#4) Extrae el estadistico t y el p-value
t_stat = res.statistic
p_value = res.pvalue

#5) Define el nivel de significancia (alpha)
alpha = 0.05

#6) Decide si rechazas H0
print("t = ", t_stat)
print("p-value = ", p_value)

if p_value < alpha:
    print("Rechazo H0: hay evidencia de que existe diferencia significativa en el rendimiento entre ambos tipos de gasolina.")
else: 
    print("No rechazo H0: no hay evidencia suficiente para decir que existe diferencia en el rendimiento.")

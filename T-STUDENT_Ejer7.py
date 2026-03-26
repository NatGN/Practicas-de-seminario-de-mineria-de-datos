# Ejercicio 7: Efecto de un fertilizante
# Un agricultor mide la altura de 10 plantas (en cm) antes de aplicar un fertilizante orgánico y vuelve a medirlas una semana después.
# Antes: [15.2, 16.0, 14.8, 15.5, 17.1, 16.4, 15.9, 16.2, 15.0, 15.7]
# Después: [15.4, 16.1, 14.9, 15.6, 17.0, 16.5, 16.0, 16.3, 15.2, 15.8]
# ¿Ha provocado el fertilizante un crecimiento significativo en la altura de las plantas en esa semana?

import numpy as np
from scipy import stats

#1) Datos: altura de las plantas antes y despues
antes = np.array([15.2, 16.0, 14.8, 15.5, 17.1, 16.4, 15.9, 16.2, 15.0, 15.7])
despues = np.array([15.4, 16.1, 14.9, 15.6, 17.0, 16.5, 16.0, 16.3, 15.2, 15.8])

#2) Calculamos la diferencia (despues - antes)
# Diferencia positiva = crecimiento
diferencia = despues - antes

#3) Valor hipotetico de la media bajo H0 (no hay crecimiento)
mu0 = 0

#4) Ejecute la prueba t de 1 muestra sobre las diferencias
res = stats.ttest_1samp(diferencia, mu0)

#5) Extrae el estadistico t y el p-value
t_stat = res.statistic
p_value = res.pvalue

#6) Define el nivel de significancia (alpha)
alpha = 0.05

#7) Decide si rechazas H0
print("t = ", t_stat)
print("p-value = ", p_value)

if p_value < alpha:
    print("Rechazo H0: hay evidencia de que el fertilizante provoco un crecimiento significativo en las plantas.")
else: 
    print("No rechazo H0: no hay evidencia suficiente para decir que hubo crecimiento significativo.")

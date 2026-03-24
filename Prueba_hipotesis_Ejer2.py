# Problema 2: Duración de Baterías de Celulares
# Un fabricante de celulares asegura que la duración promedio de sus baterías es de 20 horas. 
# Se toma una muestra de 30 baterías y se encuentra que su duración promedio es de 18.5 horas, 
# con una desviación estándar de 2.5 horas.  

# Con un nivel de significancia del 5%, ¿se puede concluir que la duración de las baterías 
# es menor a la especificada por el fabricante?  

import numpy as np
import scipy.stats as stats  
import pandas as pd


# Datos del problema
mu_0 = 20  # Hipotesis nula
n = 30  # Tamaño de la muestra
x_bar = 18.5  # Media muestral
s = 2.5  # Desviacion estandar muestral
alpha = 0.05  # Nivel de significancia

# Calculo del estadistico de prueba Z
z = (x_bar - mu_0) / (s / np.sqrt(n))

# Valor critico para prueba unilateral IZQUIERDA
z_critical = stats.norm.ppf(alpha)  # Para cola izquierda: alpha directamente

# Comparacion de los valores (prueba unilateral izquierda)
if z < z_critical:
    decision = "Rechazar hipotesis nula"
    print("Rechazar hipotesis nula: La duración es menor a 20 horas")
else:
    decision = "No rechazar la hipotesis nula"
    print("No rechazar la hipotesis nula: No hay evidencia suficiente")

# Crear un DataFrame con los datos
df = pd.DataFrame({
    'Parametros': ['Media teorica', 'Media muestral', 'Desviacion estandar', 
                   'Tamaño de muestra', 'Z-Calculado', 'Z-Critico', 'Decision'],
    'Valores': [mu_0, x_bar, s, n, round(z, 4), round(z_critical, 4), decision]
})

print("\nResumen de resultados:")
print(df)


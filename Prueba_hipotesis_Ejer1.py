# Problema 1: Control de Calidad en una Fábrica de Tornillos
# Una fábrica de tornillos afirma que el diámetro promedio de sus tornillos es de 10 mm. 
# Se toma una muestra aleatoria de 49 tornillos, obteniéndose un diámetro promedio de 9.7 mm con una desviación estándar de 0.5 mm.  

# ¿Se puede concluir, con un nivel de significancia del 1%, que el diámetro medio es menor al teórico de 10 mm?  


import numpy as np
import scipy.stats as stats  
import pandas as pd


# Datos del problema
mu_0 = 10  # Hipotesis nula
n = 49  # Tamaño de la muestra
x_bar = 9.7  # Media muestral
s = 0.5  # Desviacion estandar muestral
alpha = 0.01  # Nivel de significancia

# Calculo del estadistico de prueba Z
z = (x_bar - mu_0) / (s / np.sqrt(n))

# Valor critico para la prueba
z_critical = stats.norm.ppf(1 - alpha)

# Comparacion de los valores
decision = "Rechazar hipotesis nula" if z > z_critical else "No rechazar la hipotesis nula"

if z > z_critical:
    print("Rechazar hipotesis nula")
else:
    print("No rechazar la hipotesis nula")

# Crear un DataFrame con los datos
df = pd.DataFrame({
    'Parametros': ['Media teorica', 'Media muestral', 'Desviacion estandar', 
                   'Tamaño de muestra', 'Z-Calculado', 'Z-Critico', 'Decision'],
    'Valores': [mu_0, x_bar, s, n,z,z_critical,'Rechazar la hipotesis nula'if z> z_critical else 'No rechazar la hipotesis nula']
})

print("\nResumen de resultados:")
print(df)
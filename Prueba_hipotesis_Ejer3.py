# Problema 3: Control de Peso en una Planta de Alimentos
# Un productor de harina en bolsa indica que el peso promedio de sus bolsas es de 1 kg (1000 gramos). 
# Para verificarlo, se toman 40 bolsas y se obtiene un peso promedio de 990 gramos, con una desviación estándar de 12 gramos.  

# Si se usa un nivel de significancia del 2%, ¿se puede concluir que las bolsas tienen un peso menor al anunciado?

import numpy as np
import scipy.stats as stats  
import pandas as pd


# Datos del problema
mu_0 = 1000  # Hipotesis nula
n = 40  # Tamaño de la muestra
x_bar = 990  # Media muestral
s = 12  # Desviacion estandar muestral
alpha = 0.02  # Nivel de significancia

# Calculo del estadistico de prueba Z
z = (x_bar - mu_0) / (s / np.sqrt(n))

# Valor critico para prueba unilateral IZQUIERDA
z_critical = stats.norm.ppf(alpha)  # Para cola izquierda: alpha directamente

# Comparacion de los valores
if z < z_critical:
    decision = "Rechazar hipotesis nula"
    print("Rechazar hipotesis nula: El peso promedio es menor a 1000 gramos")
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

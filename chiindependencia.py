import numpy as np
from scipy import stats

# Tabla de frecuencias observadas
tabla = np.array([
    [40, 20],
    [30, 30]
])

# Prueba chi-cuadrado
chi2, p_value, gl, esperados = stats.chi2_contingency(tabla, correction=False)

# Imprime resultados
print(f"Chi-cuadrado = {chi2:.4f}")
print(f"p-value = {p_value:.4f}")
print(f"Grados de libertad = {gl}")
print("Frecuencias esperadas:")
print(esperados)

alpha = 0.05
if p_value < alpha:
    print("Sí hay evidencia suficiente para determinar que hacer ejercicio depende del género")
else:
    print("No hay evidencia suficiente para determinar que hacer ejercicio depende del género")


# =========================
# Ejercicio 1
# =========================

tabla1 = np.array([
    [85, 65],
    [50, 100]
])

chi21, p_value1, gl1, esperados1 = stats.chi2_contingency(tabla1, correction=False)

print("\nEjercicio 1")
print(f"Chi-cuadrado = {chi21:.4f}")
print(f"p-value = {p_value1:.4f}")
print(f"Grados de libertad = {gl1}")
print("Frecuencias esperadas:")
print(esperados1)

if p_value1 < alpha:
    print("Existe una relación significativa entre la ciudad de residencia y la preferencia de transporte")
else:
    print("No existe una relación significativa entre la ciudad de residencia y la preferencia de transporte")


# =========================
# Ejercicio 2
# =========================

tabla2 = np.array([
    [40, 20],
    [35, 45],
    [15, 45]
])

chi22, p_value2, gl2, esperados2 = stats.chi2_contingency(tabla2, correction=False)

print("\nEjercicio 2")
print(f"Chi-cuadrado = {chi22:.4f}")
print(f"p-value = {p_value2:.4f}")
print(f"Grados de libertad = {gl2}")
print("Frecuencias esperadas:")
print(esperados2)

if p_value2 < alpha:
    print("El nivel educativo está relacionado con el hábito de fumar")
else:
    print("El nivel educativo no está relacionado con el hábito de fumar")


# =========================
# Ejercicio 3
# =========================

tabla3 = np.array([
    [10, 50],
    [30, 40],
    [45, 5]
])

chi23, p_value3, gl3, esperados3 = stats.chi2_contingency(tabla3, correction=False)

print("\nEjercicio 3")
print(f"Chi-cuadrado = {chi23:.4f}")
print(f"p-value = {p_value3:.4f}")
print(f"Grados de libertad = {gl3}")
print("Frecuencias esperadas:")
print(esperados3)

if p_value3 < alpha:
    print("Existe relación entre el tipo de dieta y el nivel de colesterol")
else:
    print("No existe relación entre el tipo de dieta y el nivel de colesterol")
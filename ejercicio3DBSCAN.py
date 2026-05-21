# ==================================
# EJERCICIO 3 - Fraude bancario
# ==================================

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
from sklearn.neighbors import NearestNeighbors

# ================================
# 1. Cargar datos
# ================================

df = pd.read_csv("Clustering/ejercicio_3_fraude_bancario.csv")

print(df.head())

# ================================
# 2. Escalar datos
# ================================

scaler = StandardScaler()

datos_escalados = scaler.fit_transform(
    df[["Monto", "Hora"]]
)

# ================================
# 3. Gráfico k-distancia
# ================================

neighbors = NearestNeighbors(n_neighbors=3)

neighbors_fit = neighbors.fit(datos_escalados)

distancias, indices = neighbors_fit.kneighbors(datos_escalados)

distancias = np.sort(distancias[:,2])

plt.figure(figsize=(8,6))
plt.plot(distancias)

plt.title("Gráfico k-distancia")
plt.xlabel("Puntos")
plt.ylabel("Distancia")

plt.show()

# ================================
# 4. Aplicar DBSCAN
# ================================

modelo = DBSCAN(eps=0.5, min_samples=3)

clusters = modelo.fit_predict(datos_escalados)

df["Cluster"] = clusters

# Etiquetas
df["Estado"] = df["Cluster"].apply(
    lambda x: "Sospechosa" if x == -1 else "Normal"
)

print(df)

# ================================
# 5. Graficar transacciones
# ================================

plt.figure(figsize=(8,6))

plt.scatter(
    df[df["Cluster"] != -1]["Monto"],
    df[df["Cluster"] != -1]["Hora"],
    c=df[df["Cluster"] != -1]["Cluster"],
    cmap="plasma"
)

plt.scatter(
    df[df["Cluster"] == -1]["Monto"],
    df[df["Cluster"] == -1]["Hora"],
    color="black",
    label="Fraudes detectados"
)

plt.title("Detección de fraude con DBSCAN")
plt.xlabel("Monto")
plt.ylabel("Hora")
plt.legend()

plt.show()

# ================================
# 6. Porcentaje sospechoso
# ================================

total = len(df)

sospechosas = len(df[df["Estado"] == "Sospechosa"])

porcentaje = (sospechosas / total) * 100

print(f"\nPorcentaje sospechoso: {porcentaje:.2f}%")

# ================================
# 7. Reflexión
# ================================

print("\nREFLEXIÓN:")
print("DBSCAN detecta automáticamente valores atípicos.")
print("K-Means obliga a todos los puntos a pertenecer a un cluster.")
print("Por eso DBSCAN funciona mejor para detectar fraudes.")
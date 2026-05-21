# ==================================
# EJERCICIO 2 - Sensores ambientales
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

df = pd.read_csv("Clustering/ejercicio_2_sensores_ambientales.csv")

print(df.head())

# Ver nombres de columnas
print(df.columns)

# ================================
# 2. Escalar datos
# ================================

scaler = StandardScaler()

datos_escalados = scaler.fit_transform(
    df[["Temperatura_C", "Humedad_pct"]]
)

# ================================
# 3. Gráfico k-distancia
# ================================

neighbors = NearestNeighbors(n_neighbors=3)

neighbors_fit = neighbors.fit(datos_escalados)

distancias, indices = neighbors_fit.kneighbors(datos_escalados)

distancias = np.sort(distancias[:, 2])

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

print(df)

# ================================
# 5. Graficar clusters + anomalías
# ================================

plt.figure(figsize=(8,6))

# Clusters normales
plt.scatter(
    df[df["Cluster"] != -1]["Temperatura_C"],
    df[df["Cluster"] != -1]["Humedad_pct"],
    c=df[df["Cluster"] != -1]["Cluster"],
    cmap="viridis"
)

# Anomalías
plt.scatter(
    df[df["Cluster"] == -1]["Temperatura_C"],
    df[df["Cluster"] == -1]["Humedad_pct"],
    color="red",
    label="Anomalías"
)

plt.title("Clusters y anomalías")
plt.xlabel("Temperatura")
plt.ylabel("Humedad")
plt.legend()

plt.show()

# ================================
# 6. Comparación con K-Means
# ================================

print("\nREFLEXIÓN:")
print("K-Means no detecta anomalías directamente.")
print("DBSCAN sí detecta ruido y puntos aislados.")
print("Por eso DBSCAN es mejor para detectar datos anómalos.")
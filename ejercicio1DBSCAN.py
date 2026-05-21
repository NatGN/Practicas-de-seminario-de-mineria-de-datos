# ================================
# EJERCICIO 1 - DBSCAN
# Zonas de entrega
# ================================

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

# ================================
# 1. Cargar CSV
# ================================

df = pd.read_csv("Clustering/ejercicio_1_zonas_entrega.csv")
print(df.head())

# ================================
# 2. Graficar puntos sin clasificar
# ================================

plt.figure(figsize=(8,6))
plt.scatter(df["X"], df["Y"])

plt.title("Puntos sin clasificar")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# ================================
# 3. Aplicar DBSCAN
# ================================

modelo = DBSCAN(eps=0.8, min_samples=3)

clusters = modelo.fit_predict(df[["X", "Y"]])

# ================================
# 4. Agregar columna Cluster
# ================================

df["Cluster"] = clusters

print(df)

# ================================
# 5. Graficar clusters
# ================================

plt.figure(figsize=(8,6))

# clusters normales
plt.scatter(
    df[df["Cluster"] != -1]["X"],
    df[df["Cluster"] != -1]["Y"],
    c=df[df["Cluster"] != -1]["Cluster"],
    cmap="rainbow"
)

# outliers
plt.scatter(
    df[df["Cluster"] == -1]["X"],
    df[df["Cluster"] == -1]["Y"],
    color="black",
    label="Outliers"
)

plt.title("Clusters detectados con DBSCAN")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()

# ================================
# 6. Cantidad de zonas
# ================================

num_clusters = len(set(clusters)) - (1 if -1 in clusters else 0)

print("Cantidad de zonas detectadas:", num_clusters)
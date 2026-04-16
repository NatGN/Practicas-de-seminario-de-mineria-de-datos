import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import pandas as pd

data = {
    "Horas_estudio": [1, 2, 1.5, 8, 9, 8.5, 3, 3.5, 4],
    "Calificaciones": [2, 3, 2.5, 9, 10, 9.5, 5, 5.5, 6]
}

df = pd.DataFrame(data)

# Visualizacion inicial
plt.scatter(df["Horas_estudio"], df["Calificaciones"])
plt.xlabel("Horas de estudio")
plt.ylabel("Calificaciones")
plt.title("Datos de los estudiantes")
plt.show()

# ========== MÉTODO DEL CODO ==========
inercia = []  # Para almacenar la suma de distancias al cuadrado
k_range = range(1, 6)  # Probamos k de 1 a 5 clusters

for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=0, n_init=10)
    kmeans.fit(df)
    inercia.append(kmeans.inertia_)  # inercia_ es el "codo"

# Graficar el método del codo
plt.figure(figsize=(8, 4))
plt.plot(k_range, inercia, 'bo-')
plt.xlabel('Número de clusters (k)')
plt.ylabel('Inercia (Suma de distancias al cuadrado)')
plt.title('Método del Codo para determinar k óptimo')
plt.xticks(k_range)
plt.grid(True)
plt.show()

# ========== APLICAR K-MEANS CON EL K ÓPTIMO ==========
# Según el gráfico, el codo está en k=2 (donde la curva se dobla)
k_optimo = 2  # Lo determinas visualmente del gráfico

kmeans = KMeans(n_clusters=k_optimo, random_state=0, n_init=10)
kmeans.fit(df)

# Mostrar los centroides
centroides = kmeans.cluster_centers_
print("Centroides:")
print(centroides)

# Asignar clusters
df['Cluster'] = kmeans.labels_
print("\nDataFrame con clusters:")
print(df)

# Visualización final con clusters y centroides
plt.scatter(df["Horas_estudio"], df["Calificaciones"], c=df["Cluster"], cmap='viridis')
plt.scatter(centroides[:, 0], centroides[:, 1], marker='X', color='red', s=200, label='Centroides')
plt.xlabel("Horas de estudio")
plt.ylabel("Calificaciones")
plt.title(f"Clustering de estudiantes (k={k_optimo})")
plt.legend()
plt.show()


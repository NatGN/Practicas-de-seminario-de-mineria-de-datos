import pandas as pd
import numpy as np
from numpy import random


#Crea un array de 10 números aleatorios enteros entre 0 y 100.
array_1 = random.randint(0, 101, size=10)
print(array_1)

#Crea un array de 5 números aleatorios decimales entre 0 y 1.
array_2 = random.randint(0, 2, size=5)
print(array_2)

#Crea dos arrays de números aleatorios enteros de longitud 5 y concaténalos.
array1= random.randint(0, 50, size=5)
array2= random.randint(0, 50, size=5)

concatenado = np.concatenate((array1, array2))
print(concatenado)

#Crea un array de 10 números aleatorios enteros y sepáralo en dos arrays de 5 elementos cada uno.
array3=random.randint(0,100, size=10)
print(np.split(array3,2))

#Crea una matriz de 3x3 con números aleatorios decimales entre 0 y 1.
matriz = random.rand(3,3)
print(matriz)

#Crea un array de 10 números aleatorios enteros y selecciona 3 elementos al azar.
array4 = random.randint(0, 100, size=10)
seleccion = random.choice(array4, size=3)
print(seleccion)

#Crea un array de 10 números aleatorios enteros entre 0 y 100 y calcula la media.
array5 = random.randint(0, 101, size=10)
media = np.mean(array5)
print(media)




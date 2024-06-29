#calcular el vector estable de una matriz de n*n que introduxca el usuario

import numpy as np


#pedimos al usuario que introduzca la matriz
def m_user(n):
    matriz = []
    print(f"Introduce los elementos de la matriz de {n}x{n} fila por fila:")
    for i in range(n):
        fila = list(map(float, input(f"Fila {i+1}: ").split()))
        if len(fila) != n:
            raise ValueError(f"Cada fila debe tener exactamente {n} elementos.")
        matriz.append(fila)
    return matriz

def vector_estable(matriz):
    # Convertir la matriz a un arreglo de numpy
    matriz = np.array(matriz)

    # Calcular ls valores y vectores propios de la matriz
    valores_propios, vectores_propios = np.linalg.eig(matriz)

    # Encontrar el índice del valor propio que es 1
    indice_estable = np.where(np.isclose(valores_propios, 1))[0]

    if len(indice_estable) == 0:
        raise ValueError("La matriz no tiene un valor propio igual a 1, por lo que no tiene un vector estable.")

    # Obtener el vector
    vector_estable = np.real(vectores_propios[:, indice_estable[0]])

    # Normalizar el vector estable para que sus elementos sumen 1
    vector_estable /= np.sum(vector_estable)

    return vector_estable

# Solicitar el tamaño de la matriz al usuario
n = int(input("Introduce el tamaño de la matriz (n x n): "))

# Solicitar la matriz al usuario
matriz = m_user(n)

# Calcular el vector estable
vector = vector_estable(matriz)
print("El vector estable es:", vector)

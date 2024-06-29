#Hcer una matriz de n*n y que esta calcule la transpuesat de la matriz ingresada

def matriz_usuario(n):

    matriz = []
    print(f"Introduce los elementos de la matriz de {n}x{n} fila por fila (separados por espacios):")
    for i in range(n):
        fila = list(map(float, input(f"Fila {i+1}: ").split()))
        if len(fila) != n:
            raise ValueError(f"Cada fila debe tener exactamente {n} elementos.")
        matriz.append(fila)
    return matriz

def transponer_matriz(matriz):

    n = len(matriz)
    matriz_transpuesta = []
    for i in range(n):
        fila_transpuesta = []
        for j in range(n):
            fila_transpuesta.append(matriz[j][i])
        matriz_transpuesta.append(fila_transpuesta)
    return matriz_transpuesta

def imprimir_matriz(matriz):

    for fila in matriz:
        print(" ".join(map(str, fila)))

# Solicitar el tamaño de la matriz al usuario
n = int(input("Introduce el tamaño de la matriz (n x n): "))

# Solicitar la matriz al usuario
matriz = matriz_usuario(n)

# Calcular la matriz transpuesta
matriz_transpuesta = transponer_matriz(matriz)

# Imprimir la matriz transpuesta
print("La matriz transpuesta es:")
imprimir_matriz(matriz_transpuesta)

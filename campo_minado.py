import random

def criar_matriz(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]


def posicionar_bombas(matriz, bombas):
    rows, cols = len(matriz), len(matriz[0])
    bombas_colocadas = 0

    while bombas_colocadas < bombas:
        row = random.randint(0, rows - 1)
        col = random.randint(0, rows - 1)

        if matriz[row][col] != -1:
            matriz[row][col] = -1
            bombas_colocadas += 1

def colocar_numeros(matriz):
    rows, cols = len(matriz), len(matriz[0])

    for row in range(rows):
        for col in range(cols):
            if matriz[row][col] != -1:
                bombas_vizinhas = 0

                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if 0 <= row + i < rows and 0 <= col + j and matriz[row + i][col + j] == -1:
                            bombas_vizinhas += 1
                
                matriz[row][col] = bombas_vizinhas
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
            
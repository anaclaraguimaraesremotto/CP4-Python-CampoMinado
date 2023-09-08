import random

def criar_tabuleiro(rows, cols, bombas):
    tabuleiro = [[' ' for _ in range(cols)] for _ in range(rows)]
    bombas_colocadas = 0

    while bombas_colocadas < bombas:
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)

        if tabuleiro[row][col] != 'B':
            tabuleiro[row][col] = 'B'
            bombas_colocadas += 1

    return tabuleiro

def preencher_dicas(tabuleiro):
    rows, cols = len(tabuleiro), len(tabuleiro[0])

    for row in range(rows):
        for col in range(cols):
            if tabuleiro[row][col] != 'B':
                bombas_vizinhas = 0

                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if 0 <= row + i < rows and 0 <= col + j < cols and tabuleiro[row + i][col + j] == 'B':
                            bombas_vizinhas += 1

                if bombas_vizinhas > 0:
                    tabuleiro[row][col] = str(bombas_vizinhas)

def imprimir_tabuleiro(tabuleiro):
    rows = len(tabuleiro)

    print("Tabuleiro:")
    for row in tabuleiro:
        print(" ".join(row))

def abrir_celula(tabuleiro, descobertos, row, col):
    if row < 0 or row >= len(tabuleiro) or col < 0 or col >= len(tabuleiro[0]) or descobertos[row][col]:
        return

    descobertos[row][col] = True

    if tabuleiro[row][col] == 'B':
        return

    if tabuleiro[row][col] == ' ':
        for i in range(-1, 2):
            for j in range(-1, 2):
                abrir_celula(tabuleiro, descobertos, row + i, col + j)

def jogar():
    rows, cols, bombas = 10, 10, 10
    tabuleiro = criar_tabuleiro(rows, cols, bombas)
    descobertos = [[False for _ in range(cols)] for _ in range(rows)]
    preencher_dicas(tabuleiro)
    jogo_acabou = False

    print("Bem-vindo ao Campo Minado!\n")
    imprimir_tabuleiro(descobertos)

    while not jogo_acabou:
        try:
            row = int(input("\nInforme a linha (0-9): "))
            col = int(input("Informe a coluna (0-9): "))

            if descobertos[row][col]:
                print("Essa célula já foi descoberta. Tente novamente.")
                continue

            if tabuleiro[row][col] == 'B':
                print("Você acertou uma bomba! Fim de jogo.")
                jogo_acabou = True
            else:
                abrir_celula(tabuleiro, descobertos, row, col)
                imprimir_tabuleiro(descobertos)

                if all(all(descobertos[i][j] or tabuleiro[i][j] == 'B' for j in range(cols)) for i in range(rows)):
                    print("Parabéns! Você ganhou o jogo.")
                    jogo_acabou = True

        except (ValueError, IndexError):
            print("Entrada inválida. Tente novamente.")

if __name__ == "__main__":
    jogar()

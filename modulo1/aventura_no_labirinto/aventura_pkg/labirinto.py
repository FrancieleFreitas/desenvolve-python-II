"""
Labirinto do jogo 'Aventura no Labirinto'.
=========================================

Este módulo contém funções para criar e imprimir labirintos.
"""

import random
from rich.console import Console

console = Console()

def criar_labirinto(largura: int, altura: int) -> list[list[str]]:
    """
    Gera um labirinto aleatório.

    Parâmetros
    ----------
    largura : int
        Número de colunas do labirinto.
    altura : int
        Número de linhas do labirinto.

    Retorna
    -------
    list[list[str]]
        Labirinto representado como lista de listas de strings.
        "🟦" = parede
        " " = caminho
        "🍎" = item
        "🚩" = bandeira/meta
    """
    lab = [["🟦" for _ in range(largura)] for _ in range(altura)]

    # Criar caminhos aleatórios
    for y in range(1, altura - 1):
        for x in range(1, largura - 1):
            if random.random() > 0.2:
                lab[y][x] = " "

    # Adicionar itens
    for _ in range((largura * altura) // 10):
        x, y = random.randint(1, largura - 2), random.randint(1, altura - 2)
        if lab[y][x] == " ":
            lab[y][x] = "🍎"

    # Colocar a bandeira no canto inferior direito
    lab[altura - 2][largura - 2] = "🚩"

    return lab

def imprimir_labirinto(lab: list[list[str]], jogador_pos: tuple[int, int]) -> None:
    """
    Imprime o labirinto no terminal com o jogador.

    Parâmetros
    ----------
    lab : list[list[str]]
        Labirinto a ser impresso.
    jogador_pos : tuple[int, int]
        Posição atual do jogador (linha, coluna).
    """
    console.clear()
    for y, linha in enumerate(lab):
        linha_str = ""
        for x, celula in enumerate(linha):
            if (y, x) == jogador_pos:
                linha_str += "😺"
            else:
                linha_str += celula
        console.print(linha_str)

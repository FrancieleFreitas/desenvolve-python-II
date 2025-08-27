"""
Jogador do jogo 'Aventura no Labirinto'.
=======================================

Classe e funções para movimentar o jogador, coletar itens e atualizar pontuação.
"""

class Jogador:
    """
    Representa o jogador no labirinto.

    Atributos
    ----------
    y : int
        Linha atual do jogador.
    x : int
        Coluna atual do jogador.
    pontos : int
        Pontuação acumulada.
    """

    def __init__(self):
        """Inicializa o jogador na posição (1,1) com pontuação 0."""
        self.y = 1
        self.x = 1
        self.pontos = 0

    def mover(self, direcao: str, lab: list[list[str]]) -> None:
        """
        Move o jogador no labirinto se não houver parede.

        Parâmetros
        ----------
        direcao : str
            Direção do movimento ("UP", "DOWN", "LEFT", "RIGHT").
        lab : list[list[str]]
            Labirinto para checar colisões.

        Retorna
        -------
        None
        """
        nova_y, nova_x = self.y, self.x

        if direcao == "UP":
            nova_y -= 1
        elif direcao == "DOWN":
            nova_y += 1
        elif direcao == "LEFT":
            nova_x -= 1
        elif direcao == "RIGHT":
            nova_x += 1

        if lab[nova_y][nova_x] != "🟦":
            self.y, self.x = nova_y, nova_x
            # Coleta item se houver
            if lab[self.y][self.x] == "🍎":
                self.pontuar()
                lab[self.y][self.x] = " "

    def pontuar(self, pontos: int = 1) -> None:
        """
        Atualiza a pontuação do jogador.

        Parâmetros
        ----------
        pontos : int, opcional
            Pontos a adicionar (default=1).

        Retorna
        -------
        None
        """
        self.pontos += pontos

    def get_posicao(self) -> tuple[int, int]:
        """
        Retorna a posição atual do jogador.

        Retorna
        -------
        tuple[int, int]
            Tupla (linha, coluna) da posição.
        """
        return self.y, self.x

"""
======================================================
  AVENTURA NO LABIRINTO - DOCUMENTAÇÃO DO PROJETO
======================================================

Este pacote contém os módulos essenciais para o funcionamento do jogo
'Aventura no Labirinto', incluindo:

- Lógica para criação e impressão do labirinto
- Funções para controle do jogador
- Funções utilitárias para a interface do terminal

O jogo é uma aventura interativa em que o jogador deve encontrar a saída de um
labirinto, coletando itens e navegando por desafios.
"""

from . import jogador
from . import labirinto
from . import utils

__all__ = ["jogador", "labirinto", "utils"]


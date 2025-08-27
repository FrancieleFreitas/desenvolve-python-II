
"""
Arquivo principal do jogo 'Aventura no Labirinto'.
=================================================

Roda o jogo no terminal com menu, movimentação e música de fundo.
"""

import sys
import argparse
import pygame
from aventura_pkg.labirinto import criar_labirinto, imprimir_labirinto
from aventura_pkg.jogador import Jogador
from aventura_pkg.utils import (
    imprime_menu, imprime_instrucoes, tela_vitoria, tela_derrota, sair_jogo
)

from pynput import keyboard

def main():
    """Executa o jogo completo."""
    parser = argparse.ArgumentParser(description="Aventura no Labirinto")
    parser.add_argument("--name", type=str, required=True, help="Nome do jogador")
    parser.add_argument("--dificuldade", type=int, choices=[1,2,3], default=1, help="Dificuldade do labirinto")
    parser.add_argument("--disable-sound", action="store_true", help="Desativa música de fundo")
    args = parser.parse_args()

    largura = 8 + args.dificuldade*4
    altura = 6 + args.dificuldade*3
    lab = criar_labirinto(largura, altura)
    jogador = Jogador()

    # Inicializa música
    if not args.disable_sound:
        pygame.mixer.init()
        try:
            pygame.mixer.music.load("musica_fundo.mp3")
            pygame.mixer.music.play(-1)
        except pygame.error:
            print("Não foi possível carregar a música.")

    opcao_menu = ""
    while opcao_menu != "3":
        imprime_menu(["Instruções", "Jogar", "Sair"])
        opcao_menu = input("Escolha uma opção: ")
        match opcao_menu:
            case "1":
                imprime_instrucoes()
            case "2":
                jogando = True
                imprimir_labirinto(lab, jogador.get_posicao())

                def on_press(tecla):
                    try:
                        if tecla.char.lower() == "w":
                            jogador.mover("UP", lab)
                        elif tecla.char.lower() == "s":
                            jogador.mover("DOWN", lab)
                        elif tecla.char.lower() == "a":
                            jogador.mover("LEFT", lab)
                        elif tecla.char.lower() == "d":
                            jogador.mover("RIGHT", lab)
                        imprimir_labirinto(lab, jogador.get_posicao())

                        if lab[jogador.y][jogador.x] == "🚩":
                            tela_vitoria(args.name, jogador.pontos)
                            return False # Para o listener
                    except AttributeError:
                        pass

                with keyboard.Listener(on_press=on_press) as listener:
                    listener.join()
            case "3":
                sair_jogo()
                sys.exit()

if __name__ == "__main__":
    main()


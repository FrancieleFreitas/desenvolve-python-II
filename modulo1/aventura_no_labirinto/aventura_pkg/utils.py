
"""
Funções utilitárias para o jogo 'Aventura no Labirinto'.
========================================================

Inclui menu, instruções, tela de vitória/derrota, saída e animação recursiva.
"""

from rich.console import Console
from rich.panel import Panel
from time import sleep

console = Console()

def imprime_menu(opcoes: list[str]) -> None:
    """Imprime o menu principal formatado."""
    console.print(Panel("MENU PRINCIPAL", style="bold blue"))
    for i, opcao in enumerate(opcoes, 1):
        console.print(f"[yellow]{i}[/yellow] - {opcao}")

def imprime_instrucoes() -> None:
    """Imprime instruções do jogo."""
    console.print(Panel("INSTRUÇÕES", style="bold green"))
    console.print("Use as teclas W,A,S,D para se mover.")
    console.print("Colete os itens 🍎 para ganhar pontos.")
    console.print("Chegue na bandeira 🚩 para vencer o jogo!")

def tela_vitoria(nome: str, pontos: int) -> None:
    """Mostra tela de vitória com pontuação."""
    console.clear()
    console.print(Panel(f"🏆 PARABÉNS {nome}! 🏆\nPontuação: {pontos}", style="bold green"))
    explosao_emoji(5)

def tela_derrota(nome: str) -> None:
    """Mostra tela de derrota."""
    console.clear()
    console.print(Panel(f"💀 {nome}, você perdeu! 💀", style="bold red"))

def sair_jogo() -> None:
    """Mostra mensagem de despedida ao sair do jogo."""
    console.clear()
    console.print(Panel("👋 Saindo do jogo... Até a próxima!", style="bold yellow"))

def explosao_emoji(n: int) -> None:
    """Função recursiva que imprime emojis de celebração."""
    if n <= 0:
        return
    console.print("✨🎉✨" * n)
    sleep(0.3)
    explosao_emoji(n-1)

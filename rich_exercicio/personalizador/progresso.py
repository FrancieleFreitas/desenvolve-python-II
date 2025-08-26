"""
Módulo de progresso utilizando Rich.
Fornece funções que exibem barras de progreso da biblioteca Rich
"""

from rich.console import Console
from rich.progress import Progress, track
import time

console = Console()


def barra(texto: str, isArquivo: bool = False):
    """
    Exibe uma barra de progresso simples.
    """
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            texto = f.read()

    for _ in track(range(5), description=texto):
        time.sleep(0.5)


def passos(texto: str, isArquivo: bool = False):
    """
    Exibe uma barra de progresso com passos definidos no texto.
    Cada palavra é um passo.
    """
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            texto = f.read()

    palavras = texto.split()
    with Progress() as progresso:
        tarefa = progresso.add_task("Executando...", total=len(palavras))
        for p in palavras:
            progresso.console.print(f"[cyan]Passo:[/cyan] {p}")
            time.sleep(0.5)
            progresso.advance(tarefa)
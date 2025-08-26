"""
Módulo de painel utilizando Rich.
Fornece funções que exibem texto dentro de painéis da biblioteca rich.
"""

from rich.console import Console
from rich.panel import Panel
from rich.rule import Rule

console = Console()


def caixa(texto: str, isArquivo: bool = False):
    """
    Exibe o texto dentro de um painel.
    """
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            texto = f.read()

    console.print(Panel(texto, expand=False))


def titulo(texto: str, isArquivo: bool = False):
    """
    Exibe o texto como um título (linha com regra).
    """
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            texto = f.read()

    console.print(Rule(texto))

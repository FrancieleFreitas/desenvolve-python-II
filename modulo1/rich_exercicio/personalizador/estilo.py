"""
Módulo de estilo utilizando Rich.
Fornece funções que exibem texto estilizado com rich.
"""

from rich.console import Console

console = Console()


def info(texto: str, isArquivo: bool = False):
    """
    Exibe uma mensagem de informação.
    """
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            texto = f.read()

    console.print(f"[bold green]INFO:[/bold green] {texto}")


def erro(texto: str, isArquivo: bool = False):
    """
    Exibe uma mensagem de erro.
    """
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            texto = f.read()

    console.print(f"[bold red]ERRO:[/bold red] {texto}")